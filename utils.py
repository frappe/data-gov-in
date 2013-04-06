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
		
def get_hex_shade(color, percent):
	def p(c):
		v = int(c, 16) + int(int('ff', 16) * (float(percent)/100))
		if v < 0: 
			v=0
		if v > 255: 
			v=255
		h = hex(v)[2:]
		if len(h) < 2:
			h = "0" + h
		return h
		
	r, g, b = color[0:2], color[2:4], color[4:6]
	
	avg = (float(int(r, 16) + int(g, 16) + int(b, 16)) / 3)
	# switch dark and light shades
	if avg > 128:
		percent = -percent

	# stronger diff for darker shades
	if percent < 25 and avg < 64:
		percent = percent * 2
	
	return p(r) + p(g) + p(b)

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
			"data": [flt(val) for val in d[1:]]
		})
		i -= 30
	
	chart_data = {
		"labels": x_labels,
		"datasets": data_sets
	}
	
	return json.dumps(chart_data)
	
def flt(val):
	try:
		return float(val)
	except ValueError, e:
		return 0

def urlencode(txt):
	import urllib2
	return urllib2.quote((txt or "").encode("utf-8"))