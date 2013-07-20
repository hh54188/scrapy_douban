import pymongo
from pymongo import MongoClient

class MongoDBClas(object):
    client = MongoClient('localhost', 27017)
    db = client.test
    collection = db.douban

    def __init__(self):
        print self.collection
        pass

    def save():
        pass

db = MongoDBClas()

        