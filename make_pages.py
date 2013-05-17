from __future__ import unicode_literals

import os, sys, csv, json, re
import db, utils
from jinja2 import Environment, FileSystemLoader

def make_datasets():
	db.connect()
	for dataset in db.sql("select * from dataset limit 10", as_dict=True):
		
		# set group
		group = db.sql("select `group` from dataset_group where dataset=%s limit 1", 
			dataset["name"])[0][0]
		dataset["group_info"] = db.sql("select * from `group` where name=%s", 
			group, as_dict=True)[0]
			
		# other libs
		dataset["json"] = json
		dataset["public_path"] = "../" # all paths relative to
		
		# make page
		jenv = Environment(loader = FileSystemLoader("templates"))
		html = jenv.get_template("dataset.html").render(dataset)
		fname = re.sub(r'\W+', '', dataset["name"].lower()).replace(" ", "_") + ".html"
		with open(os.path.join("public", "datasets", fname), "w") as htmlfile:
			htmlfile.write(html)
			
		db.conn.execute("update dataset set html_filename=%s where name=%s", (fname, dataset["name"]))
			
if __name__=="__main__":
	make_datasets()
