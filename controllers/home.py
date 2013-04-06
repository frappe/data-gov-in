import os
import setproperties, utils

def get_args(form_dict):
	setproperties.load_properties()
	group_list = setproperties.groups.keys()
	group_list.sort()
	group_datasets = setproperties.get_group_datasets()
	
	maxsets = max([len(group_datasets[g]) for g in group_datasets])
	for g in setproperties.groups:
		setproperties.groups[g]["sets"] = float(len(group_datasets[g]))
			
	return {
		"group_list": group_list,
		"groups": setproperties.groups,
		"group_datasets": group_datasets,
		"get_hex_shade": utils.get_hex_shade,
		"maxsets": maxsets,
		"int": int
	}
