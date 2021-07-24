import csv
import plotly.express as px
import numpy as np

def get_data_src(data_path, row_1_name, row_2_name):
	temp_list = []
	ic_list = []

	with open(data_path) as f:
		df = csv.DictReader(f)
		for row in df:
			temp_list.append(float(row[row_1_name]))
			ic_list.append(float(row[row_2_name]))

	return {'x': ic_list, 'y': temp_list}

def find_corellation(data_src):
	corellation = np.corrcoef(data_src['x'], data_src['y'])
	return corellation

def setup():
	data1 = "data.csv"
	data2 = 'data2.csv'
	data_src_1 = get_data_src(data1, "Marks In Percentage", "Days Present")
	data_src_2 = get_data_src(data2, "sleep in hours", "Coffee in ml")
	corellation_data1 = find_corellation(data_src_1)
	corellation_data2 = find_corellation(data_src_2)

	print("Corellation between Marks and Days Preset is ", corellation_data1[0][1])
	print("Corellation between Sleep in Hours and Coffee is ", corellation_data2[0][1])


setup()