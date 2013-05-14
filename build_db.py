"""
build database and map data points against regions and periods
"""

# make database
from __future__ import unicode_literals

import MySQLdb
import getpass, os, re, json, difflib, sys
import conf, utils
from data.states import states

conn = None
debug = False

def make(filename):
	global conn
	conn = connect()
	make_db()
	if filename:
		process_file(filename)
	else:
		build()
	
	
def build():
	for fpath in os.listdir(os.path.join("data", "csv")):
		process_file(fpath)

def process_file(fpath):
	print fpath + "..."
	headers, data = utils.get_file_data(os.path.basename(fpath))
	if data and headers:
		# dataset
		insert("dataset", {
			"name": headers["title"],
			"description": headers["description"],
			"raw_filename": headers["file_name"],
			"url": headers["url"]
		})
		
		data = clean_data(data)
		set_series(headers, data)
		set_data(headers, data)

def clean_data(data):
	"""
	truncate empty rows and columns
	"""
	data = truncate_empty_rows(data)
	
	# transpose
	data = zip(*data)
	data = truncate_serial_number_row(data)
	data = truncate_empty_rows(data)
	
	# transpose back to original format
	data = zip(*data)
	
	return data

def truncate_empty_rows(data):
	newdata = []
	empty_rows = 0
	for row in data:
		if sum(map(lambda d: True if d else False, row)):
			empty_rows = 0
			newdata.append(row)
		else:
			empty_rows += 1
			if empty_rows > 2:
				# three empty rows on a trot?
				# thats it!
				break
	
	return newdata
	
def truncate_serial_number_row(data):
	row = data[0]
	to_check = min(5, len(row))
	matched = 0
	for i, value in enumerate(row[1:]):
		try:
			v = utils.flt(value)
		except ValueError:
			v = 0
		if v==utils.flt(i+1):
			matched+=1
	
	if float(matched) / to_check > 0.8:
		data = data[1:]
		
	return data

def set_series(headers, data):
	"""
	extract series from the data and guess its type
	also set headings, region, period in the db.
	first row must be a series
	for columns, there could be zero or any number of columns that are series.
	"""
	# columns
	headers["series"] = series = []
	series.append({
		"position": "column",
		"idx": 0,
		"values": [d.strip() for d in data[0]]
	})

	# transpose
	data = zip(*data)

	# rows: search for 0 or more row headers
	for i, row in enumerate(data[:-1]):
		row = row[1:]
		if is_numeric(row) and not is_series_period(row):
			break
		else:
			series.append({
				"position": "row",
				"idx": i,
				"values": [d.strip() for d in row]
			})

	# transpose back
	data = zip(*data)

	# guess row headres
	for s in series[1:]:
		guess_series(s, headers)

	# adjust column headers based on number of row-series
	row_series_count = sum(map(lambda s: s["position"]=="row" and 1 or 0, series))
	headers["row_series_count"] = row_series_count
	series[0]["values"] = series[0]["values"][row_series_count:]
	
	# guess column headers (once the rows headers have been adjusted)
	guess_series(series[0], headers)

def guess_series(s, headers):
	updated = []
	values = s["values"]
	
	if is_series_period(values):
		# period
		for value in values:
			match = re.search("[0-9]{4}[-0-9]*", value) or re.search("[0-9]{2}-[0-9]{2}", value)
			if match:
				value = match.group(0)
			insert("period", {"name": value})
			updated.append(value)
	
		# update only matched part where applicable
		s["values"] = updated
		s["type"] = "period"

	elif is_series_region(values):
		# states
		for value in values:
			matches = difflib.get_close_matches(value, states)
			value = matches[0] if matches else value
			updated.append(value)
			insert("region", {"name": value, "type": "State"})

		s["values"] = updated
		s["type"] = "region"
	else:
		for value in values:
			insert("head", {"name": value, "dataset": headers["title"]})
			
def set_data(headers, data):
	"""
	set data in the data table. set region, 
	period properties if identified in series
	"""
	start_col = headers["row_series_count"]
	series = headers["series"]

	def set_key(d, s, key, idx):
		if s.get("type")==key:
			d[key] = s["values"][idx]
			return True
		return False
	
	def set_keys_or_head(d, s, row_idx, col_idx, head_cnt):
		idx = row_idx if s["position"]=="row" else col_idx
		region = set_key(d, s, "region", idx)
		period = set_key(d, s, "period", idx)
		
		# also add as head
		if head_cnt < 5:
			d["head" + str(head_cnt)] = s["values"][idx]

	for row_idx, row in enumerate(data[1:]):
		for col_idx, value in enumerate(row[start_col:]):
			if not utils.is_number(value):
				continue
				
			d = {
				"value": value,
				"dataset": headers["title"]
			}
			
			head_cnt = 1
			for s in series:
				set_keys_or_head(d, s, row_idx, col_idx, head_cnt)
				head_cnt += 1
						
			insert("data", d)

def is_numeric(row):
	return True if sum(map(utils.is_number, row)) else False

def is_series_period(series):
	def is_year(v):
		if len(v) > 30:
			return False
		if len(v)==4 and utils.is_number(v):
			v = utils.flt(v)
			return v > 1900 and v < 2050
		else:
			matched = re.search("19[0-9]{2}[^0-9]+", v) \
				or re.search("20[0-9]{2}[^0-9]+", v) \
				or re.search("[0189][0-9]-[0189][0-9]", v)
				
			return matched
			
	matched = match_series(series, is_year)
	# if matched:
	# 	print series
	# 	raw_input("ok")
	return matched

def is_series_region(series):
	return match_series(series, lambda v: difflib.get_close_matches(v, states))

def match_series(series, rule, confidence=0.7):
	"""return true if more than 7/10 match"""	
	to_check = min(len(series), 10)
	unmatched = 0
	for i in xrange(to_check):
		if not rule(series[i]):
			unmatched += 1
		if (float(unmatched) / to_check) > (1 - confidence):
			return False

	return True
	
def make_db():
	print "making db..."
	conn.execute("drop database if exists %s" % conf.dbname)
	conn.execute("create database %s" % conf.dbname)
	conn.execute("use %s" % conf.dbname)

	# region
	conn.execute("""create table `region` (
		name varchar(180) primary key, 
		parent varchar(180) references region(name),
		type varchar(180)
		) engine=MyISAM""")

	conn.execute("""create table `category` (
		name varchar(180) primary key
		) engine=MyISAM""")

	conn.execute("""create table `period` (
		name varchar(180) primary key,
		parent varchar(180) references period(name)
		) engine=MyISAM""")

	conn.execute("""create table `dataset` (
		name varchar(180) primary key, 
		filename varchar(180),
		raw_filename varchar(180),
		url text,
		description text,
		category varchar(180) references category(name)
		) engine=MyISAM""")
	
	conn.execute("""create table `head` (
		name varchar(180) primary key,
		dataset varchar(180) references dataset(name)
		) engine=MyISAM""")	

	conn.execute("""create table `data` (
		region varchar(180) references region(name),
		period varchar(180) references period(name),
		dataset varchar(180) references datatype(name),
		head1 varchar(180) references head(name),
		head2 varchar(180) references head(name),
		head3 varchar(180) references head(name),
		head4 varchar(180) references head(name),
		value decimal(15,2)
		) engine=MyISAM""")

def insert(table, obj):
	items = obj.items()
	keys = [i[0] for i in items]
	values = [i[1] for i in items]
	if debug:
		print """insert into `%s`(%s) values 
			(%s) on duplicate key update name=name""" % (table, ", ".join(keys), 
				", ".join(['%s'] * len(values))) % tuple(values)

	conn.execute("""insert ignore into `%s`(%s) values 
		(%s)""" % (table, ", ".join(keys), 
			", ".join(['%s'] * len(values))), values)

def connect():
	if not conf.rootdbpassword:
		conf.rootdbpassword = getpass.getpass("MySQL root password: ")
		
	conn = MySQLdb.connect(user="root", host="localhost", passwd=conf.rootdbpassword, 
		use_unicode=True, charset='utf8')
	conn.converter[246]=float
	return conn.cursor()
	
if __name__=="__main__":
	make(sys.argv[1] if len(sys.argv) > 1 else None)
