import utils, setproperties

def get_args(form_data):
	setproperties.load_properties()
	return {
		"group_dataset": setproperties.get_group_datasets()[form_data["group"]],
		"group_info": setproperties.groups[form_data["group"]]
	}