from flask import Flask, url_for
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	# return 'Hello World!'
	# for i in range(10000):
	# 	print i
	return render_template('index.html')

@app.route('/login/<username>')
def login(username):
	return 'login %s' % (username)

# @app.route('/login/<username>', methods="POST")
# def login():
# 	return 'login'

app.debug = True
app.run()