from __future__ import unicode_literals
import os

def get_file_data(fname):
	if fname and not fname.startswith("."):
		import csv
		with open(os.path.join("data", "csv", fname), "r") as csv_file:
			reader = csv.reader(csv_file.read().splitlines())
			csvrows = []
			for row in reader:
				newrow = []
				csvrows.append(newrow)
				for col in row:
					for encoding in ["utf-8", "windows-1250", "windows-1252"]:
						try:
							col = unicode(col, encoding=encoding)
							break
						except UnicodeDecodeError, e:
							continue
						
						col = unicode(col, errors="ignore")
						
					newrow.append(col)
	
		return csvrows
	else:
		return None
