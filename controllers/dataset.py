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
	i = 250
	for d in transposed_data[1:]:
		data_sets.append({
			"fillColor" : "rgba(%s, %s, %s, %s)" % (i, i, i, .5),
			"strokeColor" : "rgba(%s, %s, %s, %s)" % (i, i, i, 1),
			"pointColor" : "rgba(%s, %s, %s, %s)" % (i, i, i, 1),
			"pointStrokeColor" : "#fff",
			"data": [utils.flt(val) for val in d[1:]]
		})
		i -= 30
	
	chart_data = {
		"labels": x_labels,
		"datasets": data_sets
	}
	
	return json.dumps(chart_data)
