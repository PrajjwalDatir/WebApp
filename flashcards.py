#!/usr/bin/env python

from flask import Flask, render_template
from datetime import datetime
from flask_fontawesome import FontAwesome

app = Flask(__name__)
try:
	@app.route('/')
def Welcome():
	return render_template("Website01/index.html")	
except Exception as e:
	raise e

try:
	@app.route('/date')
	def date():
		return "DATE " + str(datetime.now())
except Exception as e:
	raise e

if __name__=='__main__':
	app.run(debug=True)


