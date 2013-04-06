#!/usr/bin/env python

from __future__ import unicode_literals
import cgi, cgitb, os
from jinja2 import Environment, FileSystemLoader
from utils import get_file_data


cgitb.enable()

def render():
	form_dict = get_cgi_fields()
	fname = form_dict.get("fname")
	files = get_file_names()
	chart_data = get_chart_data(fname)
	
	
	jenv = Environment(loader = FileSystemLoader("templates"))
	template = form_dict.get("page", "home")

	html = jenv.get_template(template + ".html").render({
		"files": files,
		"fname": fname or files[0],
		"file_data": get_file_data(fname or files[0]),
		"chart_data": chart_data
	})
	
	print "Content-Type: text/html"
	print
	print (html or "").encode("utf-8")


def get_cgi_fields():
	cgi_fields = cgi.FieldStorage(keep_blank_values=True)
	form = {}
	
	for key in cgi_fields.keys():
		form[key] = cgi_fields.getvalue(key)
		
	return form
	

def get_file_names():
	file_names = [fname for fname in os.listdir(os.path.join("data", "csv")) 
		if not fname.startswith(".")]
	file_names.sort()
	return file_names
	
def get_chart_data(fname):
	import json
	file_data = get_file_data(fname or files[0])
	y_labels = file_data[0][1:]
	transposed_data = map(list, zip(*file_data))
	x_labels = transposed_data[0][1:]
	
	data_sets = []
	i = 220
	for d in transposed_data[1:]:
		data_sets.append({
			"fillColor" : "rgba(%s, %s, %s, %s)" % (i, i, i, .5),
			"strokeColor" : "rgba(%s, %s, %s, %s)" % (i, i, i, 1),
			"pointColor" : "rgba(%s, %s, %s, %s)" % (i, i, i, 1),
			"pointStrokeColor" : "#fff",
			"data": [float(val) for val in d[1:]]
		})
		i -= 100
	
	chart_data = {
		"labels": x_labels,
		"datasets": data_sets
	}
	
	return json.dumps(chart_data)
	
if __name__=="__main__":
	render()