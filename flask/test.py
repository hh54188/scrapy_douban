# -*- coding: utf-8 -*- 

import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

Connection = MongoClient("localhost", 27017);
DB = Connection.test;
Collection = DB.douban
print Collection.count()

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
