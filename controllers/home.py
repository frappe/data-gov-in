import os

def get_args(form_dict):
	file_names = [fname for fname in os.listdir(os.path.join("data", "csv")) 
		if not fname.startswith(".")]
	file_names.sort()
	return {
		"files": file_names
	}
	