# -*- coding: utf-8 -*- 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "hello"

app.config.update(
    DEBUG = True
)

if __name__ == '__main__':
    app.run(port=5000)



