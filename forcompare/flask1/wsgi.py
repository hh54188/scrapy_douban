# -*- coding: utf-8 -*- 
from flask import Flask, url_for
from flask import request
from flask import render_template
import json
import time

application = app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return "wrong"

app.config.update(
    DEBUG = True
)

if __name__ == '__main__':
    app.run(use_reloader = False)