from flask import Flask,render_template
from uuid import uuid4
import sqlite3,re,time

app = Flask(__name__)
database = 'wopr.db'

def init_db():
	con = sqlite3.connect(database)
	c = con.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS general (key TEXT, country TEXT)')
	con.commit()
	con.close()

def generate_satellite_telemetry_frame(sensor_obj,id):
	"".join([">>BEGIN TELEMETRY FRAME<<",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 ">>END TELEMETRY FRAME<<"])
def generate_polar_telemetry_frame(sensor_obj,id):
	#12 columns, 24 characters = 2 character space between columns (can widen if necessary)
	col_indicies = [0,3,]

	"".join([">>BEGIN TELEMETRY FRAME<<",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 "|@@@@@@@@@@@@@@@@@@@@@@@@|",
			 ">>END TELEMETRY FRAME<<"])
	pass

@app.route('/')
def index():
	try:
		con = sqlite3.connect(database)
		c = con.cursor()
		c.execute('SELECT * FROM general')
		r = c.fetchall()
		con.commit()
		con.close()
		return str({"status": "success", "time": time.ctime(), "DEFCON": 5, "competitors": r})+"\n"
	except Exception as e:
		return str({"status": "error", "text": str(e)})+"\n"
	#return render_template('map.html')

@app.route('/key')
def generate_new_key():
	k = uuid4()
	try:
		con = sqlite3.connect(database)
		c = con.cursor()
		c.execute('INSERT INTO general (key) VALUES (?)',(str(k),))
		con.commit()
		con.close()
		return str({"status": "success", "text": str(k)})+"\n"
	except Exception as e:
		return str({"status": "error", "text": str(e)})+"\n"

@app.route('/new_bot/country/<country>/<uuid:key>')
def bot_create_country(country,key):
	if key and country and (country != 'ussr' or country != 'usa'):
		try:
			con = sqlite3.connect(database)
			c = con.cursor()
			c.execute('UPDATE general SET country=? WHERE key=?',(country,key))
			con.commit()
			con.close()
			return str({"status": "success", "text": "Successfully created {} as {}.".format(key,country)})+"\n"
		except Exception as e:
			return str({"status": "error", "text": str(e)})+"\n"
	else:
		return str({"status": "error", "text": "Arguments invalid"})+"\n"

@app.route('/telemetry/<id>/<key>')
def stream_telemetry_data(id,key):


app.add_url_rule('/geo/move/<thing>/<mgrs>/<rate>/<key>',)
app.add_url_rule('/')

if __name__ == "__main__":
	init_db()
	app.run(host="0.0.0.0")