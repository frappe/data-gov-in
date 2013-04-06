#!/usr/bin/env python

from __future__ import unicode_literals
import cgi, cgitb, os, sys
from jinja2 import Environment, FileSystemLoader

cgitb.enable()

def render():
	form_dict = get_cgi_fields()
	fname = form_dict.get("fname")
	files = get_file_names()
	from utils import get_file_data
	
	jenv = Environment(loader = FileSystemLoader("templates"))

	html = jenv.get_template("base.html").render({
		"files": files,
		"fname": fname or files[0],
		"file_data": get_file_data(fname or files[0]),
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
	
if __name__=="__main__":
	render()
