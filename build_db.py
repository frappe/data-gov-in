# make database
from __future__ import unicode_literals

import MySQLdb
import getpass, os, re, json
import conf, utils
from data.states import states

conn = None
debug = False

def make():
	global conn
	conn = connect()
	make_db()
	build()
	
def build():
	cnt = 0
	for fpath in os.listdir(os.path.join("data", "csv")):
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
			
			set_series(headers, data)
			set_data(headers, data)

			cnt+=1
			#if cnt==10: break

def set_data(headers, data):
	"""
	set data in the data table. set region, 
	period properties if identified in series
	"""
	start_col = 2
	if headers.get("type:row_series2")=="no series":
		start_col = 1

	def set_key(d, series, tag, idx):
		if headers.get("type:" + series)==tag:
			d[tag] = headers[series][idx]
			return True
		return False
	
	def set_keys_or_head(d, series, idx):
		region = set_key(d, series, "region", idx)
		period = set_key(d, series, "period", idx)
		if not (region or period):
			if headers.get("type:" + series)!="no series":
				d["head"] = headers[series][idx]

	for row_idx, row in enumerate(data[1:]):
		for col_idx, value in enumerate(row[start_col:]):
			d = {
				"value": value,
				"dataset": headers["title"]
			}
			
			set_keys_or_head(d, "col_series", col_idx)
			set_keys_or_head(d, "row_series1", row_idx)
			set_keys_or_head(d, "row_series2", row_idx)
						
			insert("data", d)

def set_series(headers, data):
	"""
	extract series from the data and guess its type
	also set headings, region, period in the db
	"""
	# columns
	col_series = [d.strip() for d in data[0][1:]]
	
	# rows: sometimes there are two 
	# columns with headers. 
	# if there are 2 series, the first column series head is null
	row_series1 = []
	row_series2 = []
	for row in data[1:]:
		row_series1.append(row[0].strip())
		row_series2.append(row[1].strip())
		
	headers["col_series"] = col_series
	headers["row_series1"] = row_series1
	headers["row_series2"] = row_series2
	
	guess_series(headers, "col_series")
	guess_series(headers, "row_series1")
	guess_series(headers, "row_series2", True)

	# if there are 2 row-series, start column headers
	# from column 2 onwards
	if headers.get("type:row_series2")!="no series":
		headers["col_series"] = headers["col_series"][1:]

def guess_series(headers, key, check_for_values=False):
	updated = []
	series = headers[key]
	
	if check_for_values and (not False in map(lambda d: utils.is_number(d), series)):
		# all numbers, not a series
		headers["type:" + key] = "no series"
	elif re.match("[0-9]{4}[-0-9]*", series[0]):

		# period
		for s in series:
			match = re.match("[0-9]{4}[-0-9]*", s)
			if match:
				s = match.group(0)
			insert("period", {"name": s})
			updated.append(s)
	
		headers[key] = updated
		headers["type:" + key] = "period"
		
	elif len(series) > 3 and ((series[0].title() in states) or (series[1].title() in states) \
		or (series[2].title() in states)):
		# states
		for s in series:
			insert("region", {"name": s, "type": "State"})
		headers["type:" + key] = "region"
	else:
		for s in series:
			insert("head", {"name": s, "dataset": headers["title"]})
		

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
		head varchar(180) references head(name),
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
	make()