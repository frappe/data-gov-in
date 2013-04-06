from __future__ import unicode_literals
import os
import csv

def get_file_data(fname):
	filecontent = get_file_content(fname)
	if filecontent:
		reader = csv.reader(filecontent.splitlines())
		csvrows = [[col for col in row] for row in reader]
		return csvrows
	else:
		return None
		
def get_file_content(fname):
	if fname.startswith("."):
		return None
	with open(os.path.join("data", "csv", fname), "r") as datafile:
		content = datafile.read()
		for encoding in ["utf-8", "windows-1250", "windows-1252"]:
			try:
				content = unicode(content, encoding=encoding)
				break
			except UnicodeDecodeError, e:
				continue
			
			content = unicode(content, errors="ignore")
		return content


def get_chart_data(fname):
	import json
	file_data = get_file_data(fname or files[0])
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
			"data": [float(val) for val in d[1:]]
		})
		i -= 30
	
	chart_data = {
		"labels": x_labels,
		"datasets": data_sets
	}
	
	return json.dumps(chart_data)