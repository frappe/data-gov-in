from __future__ import unicode_literals

import os, json
from utils import get_file_data, get_file_content

properties = {}
propertypath = os.path.join("data", "properties.json")

def set_properties():
	global properties
	load_properties()
		
	for fname in os.listdir(os.path.join("data", "csv")):
		#data = get_file_data(fname)
		data = None
		set_property_for(fname, data)
	
	save_properties()
	
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
	fproperty = properties.get(fname, {})
	set_groups(fname, data, fproperty)
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
		if has_keyword(fname, group):
			fgroups.append(group)
				
	if not fgroups:
		file_data = get_file_content(fname)
		if has_keyword(file_data, group):
			fgroups.append(group)
		
	fproperty["groups"] = fgroups

def has_keyword(text, group):
	if not text: return
	t = text.lower()
	for keyword in groups[group]:
		if keyword in t:
			return True
			break
			
	return False
	
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
	
groups = {
	"Economy": ["economy", "gdp", "budget", "plan", "industry", "financial",
		"expenditure", "import", "export", "capita", "currency", "nrega",
		"poverty", "state", "growth", "production", "outlay", "cash",
		"transaction", "patents"],
	"Agriculture": ["crop", "wheat", "rice", "gram", "panchayat"],
	"Education": ["education", "school", "college", "skill", "employ", 
		"wage", "personnel", "graduate", "employee", "earning", "degree",
		"literacy", "workmen"],
	"Environment": ["pollution", "water", "air", "forest", "tree", "waste",
		"ozone", "chemicals", "elephant", "animal", "carbon", "parks", "temperature"],
	"Energy": ["energy", "wind", "solar", "efficient", "petroleum", "mines",
		"power", "electricity", "petrol", "diesel", "crude", "coal", "gas",
		"energies"],
	"Health": ["health", "hospital", "doctor", "born", "mortality", "birth",
		"fertility", "injury", "injuries", "allopath", "death", "medical",
		"pharma", "condom"],
	"Urban Development": ["accident", "tour", "srtu", "rural", "roads", "infrastructure"],
	"Other": []
}
	
if __name__=="__main__":
	set_properties()
	print_no_group()
	