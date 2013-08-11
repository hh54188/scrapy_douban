# -*- coding: utf-8 -*- 
import pymongo
import os
from pymongo import MongoClient

class MongoDBClas(object):

    MONGO_URL = os.environ.get('MONGOHQ_URL')
    Connection = MongoClient(MONGO_URL)
    DB = Connection.app17014052
    collection = DB.douban

    def __init__(self):
        pass

    def findAll(self):
        result = []
        for doc in self.collection.find({}):
            doc.pop("_id", None)
            result.append(doc)
        return result

    def save(self, item):
        return self.collection.insert(item) 

    def clear(self):
        return self.collection.remove()


        