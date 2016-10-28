from flask import Flask,render_template
import sqlite3,re
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('map.html')

@app.route('/new_bot/country/ussr')
def bot_create_ussr():
	pass

@app.route('/new_bot/country/usa')
def bot_create_usa(key):
	pass

@app.route('/move_<thing>/<mgrs>/<key>')
def move_thing(thing,mgrs,key):
	if mgrs:
		if re.match(r'^\d{1,2}[^ABIOYZabioyz][A-Za-z]{2}([0-9][0-9])+$',mgrs):

		else:
			return {"error": "invalid MGRS"}
	else:
		return {"error": "grid coordinate not provided"}
if __name__ == "__main__":
	app.run(host=0.0.0.0)