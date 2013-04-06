from __future__ import unicode_literals
import os, re, json
import requests
import conf

def build_message_list_from_all_files():
	message_list = []
	from utils import get_file_data
	for fname in os.listdir(os.path.join("data", "csv")):
		if not fname.startswith("agmark"):
			data = get_file_data(fname) or []
			for row in data:
				for col in row:
					if col and re.search('[a-zA-Z]+', col) \
						and not col.startswith('"') \
						and not re.search(".+@.+\.", col) \
						and not re.search("www\.", col) \
						and not re.search(".com$", col) \
						and not re.search(".in$", col):
						message_list.append(col.strip())
			
			print fname
		#if len(message_list) > 100: break
	message_list = list(set(message_list))
	message_list.sort()
		
	with open(os.path.join("data", "translations", "message_list.json"), "w") as message_list_file:
		message_list_file.write(json.dumps(message_list, indent=1, 
			sort_keys=True).encode("utf-8"))

def translate(lang):
	"""translate objects using Google API. Add you own API key for translation"""

	langfilename = os.path.join("data", "translations", lang + ".json")
	if os.path.exists(langfilename):
		with open(langfilename, 'r') as langfile:
			translations = json.loads(langfile.read())
	else:
		translations = {}

	with open(os.path.join("data", "translations", "message_list.json"), "r") as message_list_file:
		messages = json.loads(message_list_file.read())

	cnt = 0
	for m in messages:
		cnt += 1
		#if cnt > 15: break
		if not translations.get(m):
			print 'translating: ' + m
			response = requests.get("""https://www.googleapis.com/language/translate/v2""",
				params = {
					"key": conf.google_api_key,
					"source": "en",
					"target": lang,
					"q": m
				}, verify=False)

			t = response.json["data"]["translations"][0]["translatedText"] or m
			translations[m] = t.encode('utf-8')

			with open(langfilename, 'w') as langfile:
				langfile.write(json.dumps(translations, indent=1, sort_keys=True))

if __name__=="__main__":
	#build_message_list_from_all_files()
	translate("hi")