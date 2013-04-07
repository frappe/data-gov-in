import json
import utils, properties

def get_args(form_dict):
	properties.load_properties()
	file_properties = properties.properties[form_dict["fname"]]
	file_data = utils.get_file_data(form_dict["fname"])
	group = file_properties.get("groups", ["Other"])[0]
	return {
		"file_data": file_data,
		"chart_data": get_chart_data(file_data),
		"properties": file_properties,
		"group": group,
		"group_info": properties.groups[group]
	}
	
def get_chart_data(file_data):
	if not file_data:
		return
	y_labels = file_data[0][1:]
	transposed_data = map(list, zip(*file_data))
	x_labels = transposed_data[0][1:]
	
	data_sets = []
	color_steps = int(255.0 / (len(transposed_data) - 1))
	i = 0
	for d in transposed_data[1:]:
		i += color_steps
		data_sets.append({
			"fillColor" : "rgba(%i, %i, %i, %s)" % (i, i/1.2, i/4, .3),
			"strokeColor" : "rgba(%i, %i, %i, %s)" % (i, i/1.2, i/4, 1),
			"pointColor" : "rgba(%i, %i, %i, %s)" % (i, i, i/1.2, 1),
			"pointStrokeColor" : "#fff",
			"data": [utils.flt(val) for val in d[1:]]
		})
	
	chart_data = {
		"labels": x_labels,
		"datasets": data_sets
	}
	
	return json.dumps(chart_data)
