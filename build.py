"""
build database and map data points against regions and periods
"""

# make database
from __future__ import unicode_literals

import os, sys, csv
import conf, db, utils
import import_devinfo, import_data_gov_in, import_worldbank_data
from data.states import states
from data.groups import groups

db.debug = debug = False

def make(filename):
	db.connect()
	db.make()
	if filename:
		process_file(filename)
	else:
		import_groups()
		#import_data_gov_in.start()
		#import_devinfo.start()
		import_worldbank_data.start()

def import_groups():
	for g in groups:
		group_data = groups[g]
		group_data["name"] = g
		db.insert("group", group_data)

if __name__=="__main__":
	make(sys.argv[1] if len(sys.argv) > 1 else None)
