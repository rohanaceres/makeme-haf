# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoService (object):
    """ Connect to database. """
    def __init__ (self, _store_name):
        self.store_name = _store_name
        self.client = MongoClient('mongodb://localhost:27017/')

    """ Create a document inside a specific store database """
    def create (self, new_store):
        if new_store is not None:
            print (self.client[self.store_name])
            post_id = self.client[self.store_name].db.posts.insert_one(new_store.get_as_json())
            print (post_id, " created!")
        else:
            raise Exception("Nothing to save.")
    
    """ Read one document if specified, and all of them if none specified """
    def read (self, store_id):
        if store_id is None:
            return self.client[self.store_name].db.posts.find({})
        else:
            object_id = ObjectId(store_id)
            return self.client[self.store_name].db.posts.find({'_id':object_id})

    """ Update something not defined yet into the database """
    def update (self):
        print ("updating")

    """ Delete something not defined yet into the database """
    def delete (self, old_store_id):
        if old_store_id is not None:
            old_store = self.read(old_store_id)
            if (old_store[0] is not None):
                print (old_store[0])
                self.client[self.store_name].db.posts.remove(old_store[0])