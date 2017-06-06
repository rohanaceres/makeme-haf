# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoService (object):
    storeName = ''

    """ Connect to database. """
    def __init__ (self, _storeName):
        MongoService.storeName = _storeName
        self.client = MongoClient('mongodb://localhost:27017/')

    """ Create a document inside a specific store database """
    def create (self, new_store):
        if new_store is not None:
            print (self.client[self.storeName])
            post_id = self.client[self.storeName].db.posts.insert_one(new_store.get_as_json())
            print (post_id, " created!")
        else:
            raise Exception("Nothing to save.")
    
    def read (self, store_id):
        if store_id is None:
            return self.client[self.storeName].db.posts.find({})
        else:
            object_id = ObjectId(store_id)
            print (object_id)
            return self.client[self.storeName].db.posts.find({'_id':object_id})

    def update (self):
        """ Update something not defined yet into the database """
        print ("updating")

    def delete (self, id):
        """ Delete something not defined yet into the database """
        print ("deleting")