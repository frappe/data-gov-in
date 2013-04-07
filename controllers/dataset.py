import json
import utils, properties
consolelog = []

def get_args(form_dict):
	properties.load_properties()
	file_properties = properties.properties[form_dict["fname"]]
	file_data = utils.get_file_data(form_dict["fname"])
	group = file_properties.get("groups", ["Other"])[0]
	return {
		"file_data": file_data,
		"chart_data": get_chart_data(file_data, file_properties),
		"properties": file_properties,
		"group": group,
		"group_info": properties.groups[group],
		"consolelog": consolelog
	}
	
def get_chart_data(file_data, file_properties):
	global consolelog
	chart_type = file_properties.get("chart_type")
	if not chart_type:
		return
	
	data_index = file_properties["data_index"]
	x_labels = file_data[file_properties["x_axis"]][data_index:]
	map_dataset = file_data
	if file_properties["transpose"]:
		map_dataset = map(list, zip(*file_data))
		x_labels = map_dataset[file_properties["x_axis"]][data_index:]
	
	data_sets = []
	color_steps = int(255.0 / (len(map_dataset) - 1))
	i = 0
	for d in map_dataset[data_index:]:
		i += color_steps
		if chart_type == "Line":
			data_sets.append({
				"fillColor" : "rgba(%i, %i, %i, %s)" % (i, i/1.2, i/4, .3),
				"strokeColor" : "rgba(%i, %i, %i, %s)" % (i, i/1.2, i/4, 1),
				"pointColor" : "rgba(%i, %i, %i, %s)" % (i, i, i/1.2, 1),
				"pointStrokeColor" : "#fff",
				"data": [utils.flt(val) for val in d[data_index:]]
			})
		elif chart_type == "Pie":
			data_sets.append({
				"value": utils.flt(d[data_index]),
				"color": "rgba(%i, %i, %i, %s)" % (i, i/1.2, i/4, .3),
			})
	
	chart_data = {
		"chart_type": chart_type,
		"labels": x_labels,
		"datasets": data_sets
	}
		
	return json.dumps(chart_data)
