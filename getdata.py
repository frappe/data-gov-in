from __future__ import unicode_literals
import requests, re, os, xlrd, csv, cStringIO, json, urllib2
import properties

sources = [
	"http://data.gov.in/catalogs"
]

# don't downloads datasets larger than:
max_file_size = 1048576

def download():
	properties.load_properties()

	for i in range(61)[39:]:
		print "for page %s" % i
		response = requests.get(sources[0] + "?page=%s" % i, verify=False)
		page_properties = get_url_title_and_description_from_html(response.text)
		
		for filename in page_properties:
			filepath = os.path.join("data", "raw", filename)
			if not os.path.exists(filepath):
				try:
					url = urllib2.urlopen(page_properties[filename]["url"])
					size = url.headers["Content-Length"]
					if int(size) < int(max_file_size):
						with open(filepath, "wb") as datafile:
							r = requests.get(page_properties[filename]["url"])
							for chunk in r.iter_content(1024):
								datafile.write(chunk)
					else:
						print "[ignored] [too big] %s (%s)" % (filename, size)
				except urllib2.HTTPError, e:
					print e
			
			if os.path.exists(filepath):
				files = convert_to_csv(filepath)
				for fpath in files:
					prepend_property_headers(fpath, page_properties[filename])

def prepend_property_headers(fpath, properties):
	with open(fpath, "r") as csvfile:
		data = csvfile.read()

	with open(fpath, "w") as csvfile:
		csvfile.write("-----\n")
		csvfile.write(json.dumps(properties, indent=1, sort_keys=True))
		csvfile.write("\n-----\n")
		csvfile.write(data)

def get_url_title_and_description_from_html(text):
	properties = {}
	for row in text.split("ds-list-item")[1:-1]:
		row = row.replace("\n", "")
		url = re.findall("url=([^&]+)", row)[0]
		file_name = url.split("/")[-1]
		properties[file_name] = {
			"file_name": file_name,
			"url": url,
			"title": re.findall('title="([^"]+)"', row)[0],
			"description": re.findall("<br />([^<]+)", row)[0]
		}
	return properties
		
def convert_to_csv(fpath):
	import xlrd, shutil
	files = []

	fname = os.path.basename(fpath)
	extn = fpath.split(".")[-1].lower()
	
	if extn == "xls":
		wb = xlrd.open_workbook(fpath)
		sheets = wb.sheet_names()
		for i in xrange(len(sheets)):
			csv_fname = (len(sheets) > 1 and (fname[:-4] + \
				"-" + sheets[i].lower().replace(" ", "_")) or \
				fname[:-4]) + ".csv"
			sheet = wb.sheet_by_index(i)
			files.append(os.path.join("data", "csv", csv_fname))
			write_csv(sheet, csv_fname)
	elif extn == "csv":
		shutil.copy(fpath, os.path.join("data", "csv"))
		files.append(os.path.join("data", "csv", fname))
		
	return files

def write_csv(sheet, file_name):
	fpath = os.path.join("data", "csv", file_name)
	#if os.path.exists(fpath):
	#	return
	print fpath
	csv_writer = UnicodeWriter()
	for row_no in xrange(sheet.nrows):
		csv_writer.writerow(sheet.row_values(row_no))
	
	with open(fpath, "w") as csv_file:
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
	download()
	#convert_to_csv()