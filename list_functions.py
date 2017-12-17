"""
install texttable using folowing command
pip install -U git+http://github.com/bufordtaylor/python-texttable
"""
import numpy as np
import inspect
import importlib
from texttable import Texttable, get_color_string, bcolors

def __MAIN__():	
	lib_file_path = "."
	all_module_name = list_all_modules(lib_file_path)
	data_arr = create_object_array(1,2)
	data_arr = np.array(["FILE / MODULE NAME","FUNCTIONS"])
	for module_indx in xrange(len(all_module_name)):
		if (all_module_name[module_indx] != "All_Routine_Info") & (all_module_name[module_indx] != "__init__"):
			module_name = importlib.import_module(all_module_name[module_indx], package=None)
			funct_info = inspect.getmembers(module_name, inspect.isfunction)	
			funct_name =  zip(*funct_info)[0]
			funct_list = multi_line_text(funct_name)
			data_arr = np.vstack([data_arr,np.array([green_font(all_module_name[module_indx]),yellow_font(funct_list)],dtype=object)])
	print data_arr.shape
	create_table(data_arr,"l","m")

def create_table(data_arr,halign,valign):
	table_ptr = Texttable()	
	table_ptr.set_cols_align([halign]*data_arr.shape[1])
	table_ptr.set_cols_valign([valign]*data_arr.shape[1])
	for indx in xrange(data_arr.shape[0]):
		table_ptr.add_row(data_arr[indx,:])
	print 
	print(table_ptr.draw())	
	print

def green_font(inp_text):
	return get_color_string(bcolors.GREEN, inp_text)

def red_font(inp_text):
	return get_color_string(bcolors.RED, inp_text)
	
def yellow_font(inp_text):
	return get_color_string(bcolors.YELLOW, inp_text)
	
def purple_font(inp_text):
	return get_color_string(bcolors.PURPLE, inp_text)	
	
def multi_line_text(text_dict):
	l = len(text_dict)
	text = text_dict[0]
	for indx in xrange(1,l):
		text = text + "\n" + text_dict[indx]
	return text
						
def create_object_array(x_dim,y_dim):
	import numpy as np
	obj_arr = np.empty((x_dim,y_dim),dtype=object)
	return obj_arr

def list_all_modules(dir_path):
	import os
	import glob
	modules = glob.glob(dir_path +"/*.py")
	all_module_name = [ os.path.basename(f)[:-3] for f in modules]
	return all_module_name
	
__MAIN__()		
					
