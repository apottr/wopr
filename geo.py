import sqlite3

geodb = 'wopr.db'

def init_db():
	con = sqlite3.connect(geodb)
	c = con.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS geospatial (mgrs TEXT, name TEXT, side TEXT)')
	con.commit()
	con.close()

def lookup(mgrs):

	con = sqlite3.connect(geodb)
	c = con.cursor()
	c.execute('SELECT * FROM geospatial WHERE mgrs LIKE ?',('{}%{}%'.format(,)))

def move(obj,from_mgrs,to_mgrs,rate):
	pass

def place(obj,mgrs):
	pass
