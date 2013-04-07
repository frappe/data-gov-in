from __future__ import unicode_literals

import os, json
from utils import get_file_data, get_file_content

groups = {
	"Economy": {
		"label": "Macroeconomic Framework",
		"keywords": ["economy", "gdp", "budget", "plan", "industry", "financial",
			"expenditure", "import", "export", "capita", "currency", "nrega",
			"poverty", "growth", "production", "outlay", "cash",
			"transaction", "patents"],
		"icon": "icon-bar-chart",
		"color": "1D766F"
	},
	"Agriculture": {
		"label": "Agriculture and Rural Development",
		"keywords": ["crop", "wheat", "rice", "gram", "panchayat"],
		"icon": "icon-leaf",
		"color": "BF8E30"
	},
	"Education": {
		"label": "Education and Skill Development",
		"keywords": ["education", "school", "college", "skill", "employment", 
			"wage", "personnel", "graduate", "employee", "earning", "degree",
			"literacy", "workmen", "teacher"],
		"icon": "icon-book",
		"color": "A30008"
	},
	"Environment": {
		"label": "Water and Environment",
		"keywords": ["pollution", "water", "air", "forest", "tree", "waste",
			"ozone", "chemicals", "elephant", "animal", "carbon", "parks", 
			"temperature", "forests"],
		"icon": "icon-cloud",
		"color": "009D91"
	},
	"Energy": {
		"label": "Energy",
		"keywords": ["energy", "wind", "solar", "efficient", "petroleum", "mines",
			"power", "electricity", "petrol", "diesel", "crude", "coal", "gas",
			"energies"],
		"icon": "icon-lightbulb",
		"color": "FFA700"
	},
	"Health": {
		"label": "Health",
		"keywords": ["health", "hospital", "doctor", "born", "mortality", "birth",
			"fertility", "injury", "injuries", "allopath", "death", "medical",
			"pharma", "condom", "family", "deaths"],
		"icon": "icon-plus-sign-alt",
		"color": "FB000D"
	},
	"Urban Development": {
		"label": "Urban Development",
		"keywords": ["accident", "tour", "srtu", "rural", "roads", "infrastructure"],
		"icon": "icon-building",
		"color": "1D766F"
	},
	"Other": {
		"label": "Other",
		"keywords": [],
		"description": "Uncategorized",
		"icon": "icon-question-sign",
		"color": "AAAAAA"
	}
}


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
	