
from utils import get_file_data, get_chart_data

def get_args(form_dict):
	return {
		"file_data": get_file_data(form_dict["fname"]),
		"chart_data": get_chart_data(form_dict["fname"])
	}