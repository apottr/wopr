from flask import Flask,render_template
from uuid import uuid4
import sqlite3,re,time

app = Flask(__name__)
database = 'general.db'

def init_db():
	con = sqlite3.connect(database)
	c = con.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS ttbl (key TEXT, country TEXT)')
	con.commit()
	con.close()

@app.route('/')
def index():
	try:
		con = sqlite3.connect(database)
		c = con.cursor()
		c.execute('SELECT * FROM ttbl')
		r = c.fetchall()
		con.commit()
		con.close()
		return str({"status": "success", "time": time.ctime(), "DEFCON": 5, "competitors": r})+"\n"
	except:
		return str({"status": "error", "text": "database error"})+"\n"
	#return render_template('map.html')

@app.route('/key')
def generate_new_key():
	k = uuid4()
	try:
		con = sqlite3.connect(database)
		c = con.cursor()
		c.execute('INSERT INTO ttbl (key) VALUES (?)',(str(k),))
		con.commit()
		con.close()
		return str({"status": "success", "text": str(k)})+"\n"
	except Exception as e:
		return str({"status": "error", "text": str(e)})+"\n"

@app.route('/new_bot/country/<country>/<key>')
def bot_create_country(country,key):
	if key and country and (country != 'ussr' or country != 'usa'):
		try:
			con = sqlite3.connect(database)
			c = con.cursor()
			c.execute('UPDATE ttbl SET country=? WHERE key=?',(country,key))
			con.commit()
			con.close()
			return str({"status": "success", "text": "Successfully created {} as {}.".format(key,country)})+"\n"
		except:
			return str({"status": "error", "text": "SQLite3 Create Country Query failed."})+"\n"
	else:
		return str({"status": "error", "text": "Arguments invalid"})+"\n"

@app.route('/move_<thing>/<mgrs>/<key>')
def move_thing(thing,mgrs,key):
	if mgrs:
		if re.match(r'^\d{1,2}[^ABIOYZabioyz][A-Za-z]{2}([0-9][0-9])+$',mgrs):
			return str({"status": "success", "text": "valid MGRS, nothing more."})+"\n"
		else:
			return str({"status": "error", "text": "invalid MGRS"})+"\n"
	else:
		return str({"status": "error", "text": "grid coordinate not provided"})+"\n"

if __name__ == "__main__":
	init_db()
	app.run(host="0.0.0.0")