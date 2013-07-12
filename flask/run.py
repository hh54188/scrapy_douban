from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/login', methods="POST")
def login():
	return 'login'

app.debug = True
app.run()