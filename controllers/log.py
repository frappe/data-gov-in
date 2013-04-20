import os
from utils import execute_in_shell

fn_map = {
	"Apache Access Log": "get_apache_access_log"
}

def get_args(form_dict):
	args = {}
	
	if fn_map.get(form_dict.get("log_type")):
		args = globals().get(fn_map.get(form_dict.get("log_type")))(args)
	
	return args
	
def get_apache_access_log(args):
	import conf
	
	args.update({
		"properties": {
			"title": "Apache Access Log",
			"description": "Apache Access Log",
		},
		"chart_type": "Map",
		"error_log": []
	})
	
	apache_access_log_path = getattr(conf, "apache_access_log_path")
	if apache_access_log_path:
		if not os.path.exists(os.path.join("data", "logs")):
			os.makedirs(os.path.join("data", "logs"))
		
		new_access_log_path = os.path.join("data", "logs", "apache_access_log.new")
		old_access_log_path = os.path.join("data", "logs", "apache_access_log.old")
	
		if not os.path.exists(new_access_log_path):
			# touch the file
			with file(new_access_log_path, "a"):
				os.utime(new_access_log_path, None)
			
		# sync "new" into "old"
		args["error_log"].append(execute_in_shell("exec ssh-agent rsync %s %s" % (new_access_log_path, old_access_log_path)))
	
		# sync current apache access log to "new"
		args["error_log"].append(execute_in_shell("exec ssh-agent rsync %s %s" % (apache_access_log_path, new_access_log_path)))
	
		args["city_analytics"] = get_city_wise_count(old_access_log_path, new_access_log_path)
		
	return args

def get_city_wise_count(old_access_log_path, new_access_log_path):
	city_wise_count = {}
	# find new entries in "new"
	with open(old_access_log_path, "r") as old:
		with open(new_access_log_path, "r") as new:
			old_lines = old.readlines()
			new_lines = new.readlines()
			diff_lines = list(set(new_lines).difference(set(old_lines)))

			# get ip addresses
			ip_addr = []
			for l in diff_lines:
				l = l.split(" -")[0]
				if " " in l:
					l = l.split(" ")[1]
				ip_addr.append(l)
			
			# loop a set of unique ip addresses
			for ip_addr in list(set(ip_addr)):
				geoip_record = get_geoip_record(ip_addr)
				if geoip_record:
					if not city_wise_count.get(geoip_record.get("city")):
						city_wise_count[geoip_record.get("city")] = 0
					city_wise_count[geoip_record["city"]] += 1
					
	return city_wise_count

geoip = None
def get_geoip_record(ip_addr):
	global geoip
	if not geoip:
		try:
			import pygeoip
		except ImportError:
			return
	
		geoip_file = os.path.join("data", "geoip", "GeoLiteCity.dat")
		geoip = pygeoip.GeoIP(geoip_file, pygeoip.MEMORY_CACHE)

	return geoip.record_by_addr(ip_addr)

import unittest
class TestLog(unittest.TestCase):
	def test_access_log(self):
		access_log = get_args({"page": "log", "log_type": "Apache Access Log"})
		# print access_log
		self.assertTrue("city_analytics" in (access_log or {}))
		