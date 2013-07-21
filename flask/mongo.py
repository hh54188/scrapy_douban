# -*- coding: utf-8 -*- 
import pymongo
import os
from pymongo import MongoClient

class MongoDBClas(object):
    client = MongoClient('localhost', 27017)
    db = client.test
    collection = db.douban

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


        