from __future__ import unicode_literals

import os, sys, csv
import db, utils

def start():
	print "importing worldbank data..."
	db.insert("source", {"name": "World Bank"})
	utils.convert_to_csv(os.path.join("data", "worldbank", 
		"IND_Country_MetaData_en_EXCEL.xls"), os.path.join("data", "worldbank"))

	# import dataset
	with open(os.path.join("data", "worldbank", 
		"IND_Country_MetaData_en_EXCEL-sheet2.csv")) as datafile:
		reader = csv.reader(datafile.read().splitlines())
	
	for i, row in enumerate(reader):
		if i==0:
			continue
		row = [unicode(c, "utf-8", errors="ingore") for c in row]
		db.insert_dataset({
			"name": row[1][:150],
			"title": row[1],
			"description": row[2],
			"source_info": row[3],
			"source": "World Bank"
		})
		
	# import data
	with open(os.path.join("data", "worldbank", 
		"IND_Country_MetaData_en_EXCEL-sheet1.csv")) as datafile:
		reader = csv.reader(datafile.read().splitlines())

	db.insert("region", {"name": "India"})
		
	for i, row in enumerate(reader):
		if i==0:
			headers = row
			for year in row[2:]:
				db.insert("period", {"name": year})
				
		else:
			for ci, value in enumerate(row):
				if ci > 1 and utils.flt(value):
					db.insert("data", {
						"dataset": row[0],
						"period": headers[ci],
						"value": value,
						"region": "India",
					})
			if i % 100 == 0: 
				sys.stdout.write(".")
				sys.stdout.flush()
