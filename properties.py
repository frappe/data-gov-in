from __future__ import unicode_literals

import os, json
from utils import get_file_data, get_file_content

from data.groups import groups

properties = {}
propertypath = os.path.join("data", "properties.json")

def set_properties():
	global properties
	load_properties()
		
	for fname in os.listdir(os.path.join("data", "csv")):
		if not fname.startswith("."):
			data = get_file_data(fname)
			#data = None
			set_property_for(fname, data)
	
	save_properties()
	make_group_datasets()
	
def save_properties():
	with open(propertypath, "w") as propertyfile:
		propertyfile.write(json.dumps(properties, indent=1, sort_keys=True))	

def load_properties():
	global properties
	if os.path.exists(propertypath):
		with open(propertypath, "r") as propertyfile:
			properties = json.loads(propertyfile.read())
	
def set_property_for(fname, data):
	global properties
	print fname
	fproperty = properties.get(fname, {})
	set_groups(fname, data, fproperty)
	fproperty["rows"] = data and len(data) or 0
	properties[fname] = fproperty

def update_for_file(raw_fname, for_update):
	global properties
	for key in properties:
		if key.startswith(raw_fname.split(".")[0]):
			properties[key].update(for_update)

def set_groups(fname, data, fproperty):
	fgroups = []
	# set group
	for group in groups:
		if has_keyword(fproperty.get("title", fname), group):
			fgroups.append(group)
				
	if not fgroups:
		if has_keyword(fproperty.get("description", ""), group):
			fgroups.append(group)
		
	fproperty["groups"] = fgroups

def has_keyword(text, group):
	if not text: return
	t = text.lower().replace("_", " ").split()
	return set(t).intersection(set(groups[group]["keywords"]))

def get_group_datasets():
	with open(os.path.join("data", "groups.json"), "r") as groupfile:
		return json.loads(groupfile.read())
		
def make_group_datasets():	
	group_datasets = {}
	for group in groups:
		group_datasets[group] = []
	
	for fname in properties:
		p = properties[fname]
		if not p.get("title"):
			p["title"] = fname
		p["file_name"] = fname
		if p.get("groups"):
			for group in p.get("groups"):
				group_datasets[group].append(p)
		else:
			group_datasets["Other"].append(p)
	
	with open(os.path.join("data", "groups.json"), "w") as groupfile:
		groupfile.write(json.dumps(group_datasets, indent=1, sort_keys=True))

def print_no_group():
	global properties
	load_properties()

	cnt = 0
	files = properties.keys()
	files.sort()
	for p in files:
		if not properties[p].get("groups"):
			cnt += 1
			print p
			
	print "Un-categorized: ", cnt

if __name__=="__main__":
	set_properties()
	print_no_group()
	