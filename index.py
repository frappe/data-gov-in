#!/usr/bin/env python

from __future__ import unicode_literals
import cgi, cgitb, os
from jinja2 import Environment, FileSystemLoader
from utils import get_file_data

cgitb.enable()

def render():
	form_dict = get_cgi_fields()

	jenv = Environment(loader = FileSystemLoader("templates"))
	set_jenv_filters(jenv)
	
	template = form_dict.get("page", "home")
	args = get_method("controllers." + template + ".get_args")(form_dict)
	args.update(form_dict)

	html = jenv.get_template(template + ".html").render(args)

	print "Content-Type: text/html"
	print
	print (html or "").encode("utf-8")

def get_method(method_string):
	modulename = '.'.join(method_string.split('.')[:-1])
	methodname = method_string.split('.')[-1]

	__import__(modulename)
	import sys
	moduleobj = sys.modules[modulename]
	return getattr(moduleobj, methodname)

def get_cgi_fields():
	cgi_fields = cgi.FieldStorage(keep_blank_values=True)
	form = {}
	
	for key in cgi_fields.keys():
		form[key] = cgi_fields.getvalue(key)
		
	return form	
	
def set_jenv_filters(jenv):
	from utils import urlencode
	jenv.filters["urlencode"] = urlencode
	
if __name__=="__main__":
	render()
