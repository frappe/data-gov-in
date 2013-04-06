from __future__ import unicode_literals
import requests, re, os, xlrd, csv, cStringIO

sources = [
	"http://data.gov.in/hackathon/sectors",
	"http://data.gov.in/catalogs"
]

def download():
	for i in xrange(35):
		print "page %s" % i
		response = requests.get(sources[0] + "?page=%s" % i, verify=False)
		for filename in re.findall("url=([^&]+)", response.text):
			print filename
			filepath = os.path.join("data", "raw", filename.split("/")[-1])
			if not os.path.exists(filepath):
				with open(filepath, "wb") as datafile:
					r = requests.get(filename)
					for chunk in r.iter_content(1024):
						datafile.write(chunk)

def convert_to_csv():
	import xlrd, shutil
	raw_path = os.path.join("data", "raw")
	for fname in os.listdir(raw_path):
		fpath = os.path.join(raw_path, fname)
		extn = fname.split(".")[-1].lower()
		if extn == "xls":
			print fpath
			wb = xlrd.open_workbook(fpath)
			sheets = wb.sheet_names()
			for i in xrange(len(sheets)):
				file_name = (len(sheets) > 1 and (".".join(fname.split(".")[:-1]) + \
					"-" + sheets[i].lower().replace(" ", "_")) or \
					".".join(fname.split(".")[:-1])) + ".csv"
				sheet = wb.sheet_by_index(i)
				write_csv(sheet, file_name)
		elif extn == "csv":
			print fpath
			shutil.copy(fpath, os.path.join("data", "csv"))

			
def write_csv(sheet, file_name):
	if os.path.exists(os.path.join("data", "csv", file_name)):
		return
	csv_writer = UnicodeWriter()
	for row_no in xrange(sheet.nrows):
		csv_writer.writerow(sheet.row_values(row_no))
	
	with open(os.path.join("data", "csv", file_name), "w") as csv_file:
		csv_file.write(csv_writer.getvalue())

class UnicodeWriter:
	def __init__(self, encoding="utf-8"):
		self.encoding = encoding
		self.queue = cStringIO.StringIO()
		self.writer = csv.writer(self.queue, quoting=csv.QUOTE_NONNUMERIC)
	
	def writerow(self, row):
		row = self.encode(row, self.encoding)
		self.writer.writerow(row)
	
	def getvalue(self):
		return self.queue.getvalue()
	
	def encode(self, obj, encoding="utf-8"):
		if isinstance(obj, list):
			out = []
			for o in obj:
				if isinstance(o, unicode):
					out.append(o.encode(encoding))
				else:
					out.append(o)
			return out
		elif isinstance(obj, unicode):
			return obj.encode(encoding)
		else:
			return obj

if __name__=="__main__":
	#download()
	convert_to_csv()