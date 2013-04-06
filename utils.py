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
