from __future__ import unicode_literals
import requests, re, os, csv, json, urllib2
import properties
from utils import convert_to_csv

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
			filepath = os.path.join("data", "data.gov.in", filename)
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
				files = convert_to_csv(filepath, os.path.join("data", "csv"))
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
		

if __name__=="__main__":
	download()
