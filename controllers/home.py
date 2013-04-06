import os
import setproperties

def get_args(form_dict):
	setproperties.load_properties()
	group_list = setproperties.groups.keys()
	group_list.sort()
	group_datasets = {}
	for group in group_list:
		group_datasets[group] = []
	
	for fname in setproperties.properties:
		p = setproperties.properties[fname]
		if not p.get("title"):
			p["title"] = fname
		p["file_name"] = fname
		if p.get("groups"):
			for group in p.get("groups"):
				group_datasets[group].append(p)
		else:
			group_datasets["Other"].append(p)
			
	return {
		"group_list": group_list,
		"groups": setproperties.groups,
		"group_datasets": group_datasets
	}
