import properties, utils

def get_args(form_dict):
	properties.load_properties()
	group_list = properties.groups.keys()
	group_list.sort()
	group_datasets = properties.get_group_datasets()
	
	maxsets = max([len(group_datasets[g]) for g in group_datasets])
	for g in properties.groups:
		properties.groups[g]["sets"] = float(len(group_datasets[g]))
			
	return {
		"group_list": group_list,
		"groups": properties.groups,
		"group_datasets": group_datasets,
		"get_hex_shade": utils.get_hex_shade,
		"maxsets": maxsets,
		"int": int
	}
