# -*- coding: utf-8 -*-

"""
PyMongo: database used.
ObjectId: responsible for generate new IDs (PK) for an object.
"""
from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoService(object):
    """
    Responsible for the mongo database access.
    """
    def __init__(self, _store_name):
        """
        Connect to database.
        """
        self.store_name = _store_name
        self.client = MongoClient('mongodb://localhost:27017/')

    def create(self, new_store):
        """
        Create a document inside a specific store database
        """
        if new_store is not None:
            print(self.client[self.store_name])
            post_id = self.client[self.store_name].db.posts.insert_one(new_store.get_as_json())
            print(post_id, " created!")
        else:
            raise Exception("Nothing to save.")
    def read(self, store_id):
        """
        Read one document if specified, and all of them if none specified.
        """
        if store_id is None:
            return self.client[self.store_name].db.posts.find({})
        else:
            object_id = ObjectId(store_id)
            return self.client[self.store_name].db.posts.find({'_id':object_id})
    def update(self):
        """
        Update something not defined yet into the database.
        """
        print("updating")
    def delete(self, old_store_id):
        """
        Delete something not defined yet into the database.
        """
        if old_store_id is not None:
            old_store = self.read(old_store_id)
            if old_store[0] is not None:
                print(old_store[0])
                self.client[self.store_name].db.posts.remove(old_store[0])
