from flask import Flask

app = Flask(__name__)

@app.route('/a_<one>/<two>')
def index(one,two):
	return str([one,two])


if __name__ == "__main__":
	app.run()