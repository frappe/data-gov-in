from __future__ import unicode_literals
import os, csv, json

def convert_to_csv(fpath, target_path = None):
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
			csv_fpath = os.path.join(target_path, csv_fname)
			files.append(csv_fpath)
			write_csv(sheet, csv_fpath)
	elif extn == "csv":
		if target_path:
			shutil.copy(fpath, target_path)
			files.append(os.path.join(target_path, fname))
		
	return files

def get_file_data(fname):
	content = get_file_content(fname)
	separator = "-----\n".encode("utf-8")
	if content:
		if content.startswith(separator):
			t, headers, content = content.split(separator)
			headers = json.loads(headers)
		else:
			headers = {}
		reader = csv.reader(content.splitlines())
		csvrows = [[col for col in row] for row in reader]
		return headers, csvrows
	else:
		return None, None
		
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

def is_number(s):
	try:
		float(s or "0")
		return True
	except ValueError:
		return False

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
    
def execute_in_shell(cmd, verbose=0):
	# using Popen instead of os.system - as recommended by python docs
	from subprocess import Popen
	import tempfile
	
	# using tempfile.TemporaryFile since PIPE buffer is only of 65K
	with tempfile.TemporaryFile() as stdout:
		with tempfile.TemporaryFile() as stderr:
			p = Popen(cmd, shell=True, stdout=stdout, stderr=stderr)
			p.wait()
			
			stdout.seek(0)
			out = stdout.read()
			
			stderr.seek(0)
			err = stderr.read()

	if verbose:
		if err: print err
		if out: print out

	return err, out
	
def write_csv(sheet, fpath):
	print fpath
	csv_writer = UnicodeWriter()
	for row_no in xrange(sheet.nrows):
		csv_writer.writerow(sheet.row_values(row_no))
	
	with open(fpath, "w") as csv_file:
		csv_file.write(csv_writer.getvalue())

class UnicodeWriter:
	def __init__(self, encoding="utf-8"):
		from cStringIO import StringIO
		self.encoding = encoding
		self.queue = StringIO()
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
