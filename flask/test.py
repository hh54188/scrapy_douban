# -*- coding: utf-8 -*- 
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.test

print "The MongoDB is:-------->"
print db

@app.route('/')
def welcome():
    return "hello"

app.config.update(
    DEBUG = True
)

if __name__ == '__main__':
    app.run(port=5000)



