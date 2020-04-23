#!/usr/bin/env python
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

#Removed those Try-Catch for Main routes

@app.route('/')
def Welcome():
    return render_template("Website01/index.html")


@app.route('/date')
def date():
    return "DATE " + str(datetime.now())


if __name__ == '__main__':
    app.run(debug=True)

