# -*- coding: utf-8 -*- 
from flask import Flask, url_for
from flask import request
from flask import render_template
from blinker import *


app = Flask(__name__) 

@app.route('/')
def welcome():
    return "OK"

app.config.update(
    DEBUG = True
)

if __name__ == '__main__':
    app.run(use_reloader = False)
