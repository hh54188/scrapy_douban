# -*- coding: utf-8 -*- 

import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URL = "mongodb://li:guangyi@dharma.mongohq.com:10010/app17014052"
Connection = MongoClient(MONGO_URL)
DB = Connection.app17014052
collection = DB.TestDB

def count():

    return collection.count()

@app.route('/')
def welcome():
    global collection
    return str(collection.count())

@app.errorhandler(404)
def page_not_found(error):
    return "wrong"

if __name__ == '__main__':
    app.run()
