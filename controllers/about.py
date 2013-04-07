import properties, utils

def get_args(form_data):
	properties.load_properties()
	group_list = properties.groups.keys()
	group_list.sort()

	return {
		"group_list": group_list,
		"groups": properties.groups
	}