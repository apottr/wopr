import sqlite3

geodb = 'wopr.db'

def init_db():
	con = sqlite3.connect(geodb)
	c = con.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS geospatial (mgrs TEXT UNIQUE, name TEXT, side TEXT)')
	con.commit()
	con.close()

def mgrs_to_object(mgrs):
	if not mgrs[1:2].lower() in 'abcdefghijklmnopqrstuvwxyz':
		grid_zone_designator = mgrs[:2]
		grid_square_id = mgrs[2:4]
		easting_northing = mgrs[4:len(mgrs)]
	else:
		grid_zone_designator = mgrs[:3]
		grid_square_id = mgrs[3:5]
		easting_northing = mgrs[5:len(mgrs)]

	return {"grid_zone_designator": grid_zone_designator, 
		"grid_square_id": grid_square_id, "easting_northing": easting_northing}


def generate_lookup_query(mgrs):
	mgrs_obj = mgrs_to_object(mgrs)
	if len(mgrs_obj['easting_northing']) != 10:
		easting = mgrs_obj['easting_northing'][:len(easting_northing)/2]
		northing = mgrs_obj['easting_northing'][len(easting):len(mgrs_obj['easting_northing'])]
		first = mgrs_obj['grid_zone_designator']+mgrs_obj['grid_square_id']+easting
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

def in_mgrs_range(mgrs,start,end):
	mgrs_obj = mgrs_to_object(mgrs)
	alph = 'abcdefghijklmnopqrstuvwxyz'
	letter = mgrs_obj['grid_zone_designator'][-1].lower()
	numbers = mgrs_obj['grid_zone_designator'][:-1]
	start_letter = start[-1].lower()
	end_letter = end[-1].lower()
	letter_in = (letter in alph[alph.index(start_letter):alph.index(end_letter)])
	num_in = (numbers in range(start[:-1],end[:-1]))
	return letter_in and num_in

def valid_placement(obj,mgrs,side):
	land = json.loads(open('./objects/land.json').read())
	gzd = mgrs_to_object(mgrs)['grid_zone_designator']
	if 'space' in obj['type']:
		return 1
	else:
		for item in land[gzd[-1]]:
			if in_mgrs_range(mgrs,item['start'],item['end']) and 'land' in obj['type']:
				if item['side'] == side:
					return 1
				else:
					return 2
			elif 'air' in obj['type']:
					if item['side'] == side:
						return 1
					else:
						return 2
			elif 'sea' in obj['type'] and not in_mgrs_range(mgrs,item['start'],item['end']):
					if item['side'] == side:
						return 1
					else:
						return 2
		return -1

def move(obj,from_mgrs,to_mgrs,rate):
	pass

def place(obj,mgrs,side):
	con = sqlite3.connect(geodb)
	c = con.cursor()
	c.execute('INSERT INTO geospatial (mgrs,name,side) VALUES (?,?,?)',(mgrs,obj,side))
	con.commit()
	con.close()

