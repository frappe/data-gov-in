from __future__ import unicode_literals

import MySQLdb
import conf, getpass, json

from data.groups import groups

conn = None
debug = None

def make():
	print "making db..."
	conn.execute("drop database if exists %s" % conf.dbname)
	conn.execute("create database %s" % conf.dbname)
	conn.execute("use %s" % conf.dbname)

	# region
	conn.execute("""create table `region` (
		name varchar(255) primary key, 
		parent varchar(255) references region(name),
		type varchar(255)
		) engine=MyISAM""")

	conn.execute("""create table `group` (
		name varchar(50) primary key,
		label varchar(255),
		color varchar(255),
		keywords text,
		description text,
		icon varchar(255)
		) engine=MyISAM""")

	conn.execute("""create table `period` (
		name varchar(255) primary key,
		parent varchar(255) references period(name)
		) engine=MyISAM""")

	conn.execute("""create table `source` (
		name varchar(255) primary key
		) engine=MyISAM""")

	conn.execute("""create table `dataset` (
		name varchar(150) primary key, 
		source varchar(255) references source(name),
		title varchar(255),
		filename varchar(255),
		raw_filename varchar(255),
		html_filename varchar(255),
		url text,
		description text,
		source_info text
		) engine=MyISAM""")

	conn.execute("""create table `dataset_group` (
		dataset varchar(255) not null references dataset(name),
		`group` varchar(50) not null references `group`(name),
		constraint unique(dataset, `group`)
		) engine=MyISAM""")
			
	conn.execute("""create table `head` (
		name varchar(150) primary key,
		title varchar(255),
		dataset varchar(255) references dataset(name)
		) engine=MyISAM""")	

	conn.execute("""create table `data` (
		id int(15) primary key auto_increment,
		region varchar(255) references region(name),
		period varchar(255) references period(name),
		dataset varchar(255) references datatype(name),
		unit varchar(255),
		value decimal(25,2)
		) engine=MyISAM""")

	conn.execute("""create table `data_head` (
		data varchar(150) not null references data(name),
		`head` varchar(150) not null references `head`(name),
		constraint unique (data, head)
		) engine=MyISAM""")
		
def connect():
	global conn
	if not conf.rootdbpassword:
		conf.rootdbpassword = getpass.getpass("MySQL root password: ")
		
	connection = MySQLdb.connect(user="root", host="localhost", passwd=conf.rootdbpassword, 
		use_unicode=True, charset='utf8')
	connection.converter[246]=float
	conn = connection.cursor()
	
	try:
		conn.execute("use %s" % conf.dbname)
	except Exception, e:
		# not created?
		pass
	
def insert(table, obj):
	items = obj.items()
	keys = [i[0] for i in items]
	values = [i[1] for i in items]
	values = [",".join(i) if type(i)==list else i for i in values]
	if debug:
		print """insert into `%s`(%s) values 
			(%s) on duplicate key update name=name""" % (table, ", ".join(["`%s`" % k for k in keys]), 
				", ".join(['%s'] * len(values))) % tuple(values)

	conn.execute("""insert ignore into `%s`(%s) values 
		(%s)""" % (table, ", ".join(["`%s`" % k for k in keys]), 
			", ".join(['%s'] * len(values))), values)

def sql(query, values=None, as_dict=False):
	if query[:6].lower() != "select":
		query = "select " + query
	conn.execute(query, values)
	data = conn.fetchall()
	if as_dict:
		names = [i[0] for i in conn.description]
		data = [dict(zip(names, d)) for d in data]
		
	return data

def insert_dataset(d):
	group_set = False
	# find in name
	for g in groups:
		if has_keyword(d.get("title", d["name"]), g):
			insert("dataset_group", {"dataset": d["name"], "group":g})
			group_set = True
	
	# find in description
	if not group_set and d.get("description"):
		if has_keyword(d["description"], g):
			insert("dataset_group", {"dataset": d["name"], "group":g})
			group_set = True
			
	if not group_set:
		insert("dataset_group", {"dataset": d["name"], "group": "Other"})
	
	d["title"] = d["name"]
	d["name"] = d["name"][:150]
	insert("dataset", d)


def has_keyword(text, group):
	if not text: return
	t = text.lower().replace("_", " ").split()
	return set(t).intersection(set(groups[group]["keywords"]))

