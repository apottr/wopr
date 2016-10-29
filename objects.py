import sqlite3,json

obj_db = 'wopr.db'
#obj_table = 'objects'
#object_directory = './objects/'

def init_db():
	pass

def create_object(json):
	if 'air' in json['type']:
		pass
	elif 'sea' in json['type']:
		pass
	elif 'land' in json['type']:
		pass
	elif 'space' in json['type']:
		pass

def load_objects_from_files():
	pass

def modify_object(obj_name,key,value):
	pass

def get_object_properties(obj_name):
	pass