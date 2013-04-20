#!/usr/bin/env python

from __future__ import unicode_literals
import cgi, cgitb, os
from jinja2 import Environment, FileSystemLoader

# enable traceback manager for cgi
cgitb.enable()

def render():
	form_dict = get_cgi_fields()
	
	# prepare jinja environment
	jenv = Environment(loader = FileSystemLoader("templates"))
	set_jenv_filters(jenv)
	
	# get template and arguments to be passed to it
	template = form_dict.get("page", "home")
	args = get_method("controllers." + template + ".get_args")(form_dict)
	args.update(form_dict)
	
	if form_dict.get("format") == "json":
		import json
		html = json.dumps(args, default=json_handler)
	else:
		html = jenv.get_template(template + ".html").render(args)

	print "Content-Type: text/html; charset: utf-8"
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
	"""import these python functions as jinja filters"""
	from utils import urlencode
	jenv.filters["urlencode"] = urlencode
	
def json_handler(obj):
	"""serialize non-serializable data for json"""
	import datetime
	from types import ModuleType
	
	# serialize date
	if isinstance(obj, (datetime.date, datetime.timedelta, datetime.datetime)):
		return unicode(obj)
	elif hasattr(obj, "__call__") or isinstance(obj, ModuleType):
		return obj.__name__
	else:
		raise TypeError, """Object of type %s with value of %s is not JSON serializable""" % \
			(type(obj), repr(obj))
	
if __name__=="__main__":
	render()
