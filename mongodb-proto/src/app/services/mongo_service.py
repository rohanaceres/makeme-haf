# -*- coding: utf-8 -*-

from pymongo import MongoClient

class MongoService (object):
    storeName = ""

    def __init__ (self, _storeName):
        """ Connect to database. """
        MongoService.storeName = _storeName
        self.client = MongoClient('mongodb://localhost:27017/')

    def insert (self, json_to_post):
        """ Create database with mocks from database_injector """
        db = self.client[MongoService.storeName]
        post_id = db.posts.insert_one(json_to_post).inserted_id
        print (post_id, " created!")

    def get (self, field):
        db = self.client[MongoService.storeName]
        name = db.posts.find_one(field)
        return name

    def update (self):
        """ Update something not defined yet into the database """
        print ("updating")

    def delete (self, id):
        """ Delete something not defined yet into the database """
        print ("deleting")