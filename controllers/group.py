import utils, properties

def get_args(form_data):
	properties.load_properties()
	return {
		"group_dataset": properties.get_group_datasets()[form_data["group"]],
		"group_info": properties.groups[form_data["group"]]
	}