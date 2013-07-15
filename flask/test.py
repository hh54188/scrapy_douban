from flask import Flask, url_for
from flask import request
from flask import render_template
import json
import time
from info import *

app = Flask(__name__)

print "Hello World!"

app.config.update(
    DEBUG = True,
    SERVER_NAME = "127.0.0.1:8000"
)

if __name__ == '__main__':
    app.run(use_reloader=False)
