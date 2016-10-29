from flask import Flask

app = Flask(__name__)

def index(one,two):
	return str([one,two])

app.add_url_rule('/<one>/<two>','index',index)

if __name__ == "__main__":
	app.run()