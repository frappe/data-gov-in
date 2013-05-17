from __future__ import unicode_literals

import os, sys, csv
import db

def start():
	print "reading devinfo file"
	with open(os.path.join("data", "devinfo", "DevInfo India_2011_en.csv"), "r") as datafile:
		reader = csv.reader(datafile.read().splitlines())

	db.insert("source", {"name": "DevInfo India"})
	
	columns = {
		"dataset": 0,
		"unit":1,
		"head": 2,
		"region": 3,
		"region_id":4,
		"period": 5,
		"source": 6,
		"value":7,
		"footnotes":8
	}
	
	for i, row in enumerate(reader):
		if i==0: 
			continue
			
		row = [unicode(c, errors="ignore") for c in row]
			
		db.insert_dataset({
			"name": row[columns["dataset"]], 
			"title": row[columns["dataset"]],
			"source": "DevInfo India"
		})
		db.insert("region", {"name": row[columns["region"]]})
		db.insert("period", {"name": row[columns["period"]]})
				
		db.insert("data", {
			"unit": row[columns["unit"]],
			"value": row[columns["value"]],
			"dataset": row[columns["dataset"]],
			"region": row[columns["region"]],
			"period": row[columns["period"]],
		})
		
		d_id = db.sql("last_insert_id()")[0][0]
		
		if row[columns["head"]]:
			db.insert("head", {"name": row[columns["head"]]})
			db.insert("data_head", {"data": d_id, "head": row[columns["head"]]})
		
		if i % 1000==0:
			sys.stdout.write(".")
			sys.stdout.flush()
