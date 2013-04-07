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
		return content.encode("utf-8")
		
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
	
def flt(val):
	try:
		return float(val)
	except ValueError, e:
		return 0

def urlencode(txt):
	import urllib2
	return urllib2.quote((txt or "").encode("utf-8"))
