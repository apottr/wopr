import sqlite3

geodb = 'wopr.db'

def init_db():
	con = sqlite3.connect(geodb)
	c = con.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS geospatial (mgrs TEXT UNIQUE, id TEXT, side TEXT)')
	con.commit()
	con.close()

def generate_lookup_query(mgrs):
	grid_zone_designator = mgrs[:2]
	grid_square_id = mgrs[2:4]
	easting_northing = mgrs[4:len(mgrs)]
	if len(easting_northing) != 10:
		easting = easting_northing[:len(easting_northing)/2]
		northing = easting_northing[len(easting):len(easting_northing)]
		first = grid_zone_designator+grid_square_id+easting
		return '{}%{}%'.format(first,northing)
	else:
		return mgrs

def lookup(mgrs):
	con = sqlite3.connect(geodb)
	c = con.cursor()
	c.execute('SELECT * FROM geospatial WHERE mgrs LIKE ?',(generate_lookup_query(mgrs)))
	r = c.fetchall()
	con.commit()
	con.close()
	return r

def _move(obj,from_mgrs,to_mgrs):
	con = sqlite3.connect(geodb)
	c = con.cursor()
	c.execute('UPDATE geospatial SET mgrs=?,name=? WHERE mgrs=? AND name=?',(to_mgrs,obj,from_mgrs,obj))
	con.commit()
	con.close()

def place(obj,mgrs,side):
	con = sqlite3.connect(geodb)
	c = con.cursor()
	c.execute('INSERT INTO geospatial (mgrs,name,side) VALUES (?,?,?)',(mgrs,obj,side))
	con.commit()
	con.close()

