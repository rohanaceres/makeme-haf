# -*- coding: utf-8 -*-

import sys
import json
from app.services import mongo_service
from app.mocking.database_mocker import mock_amazon, mock_bestbuy

appconfig = 'appconfig.json'

def go_for_it_girl (argv):
    mongo = mongo_service.MongoService(get_store_name())

    if argv[0] == 'create':
        if len(argv) > 1:
            if argv[1].lower() == 'amazon':
                # Insert mocked model into the database
                mongo.create(mock_amazon())
            elif argv[1].lower() == 'bestbuy':
                # Insert mocked model into the database
                mongo.create(mock_bestbuy())

    elif argv[0] == 'update':
        # Update data
        pass

    elif argv[0] == 'delete':
        # Delete something
        if len(argv) > 1:
            r = mongo.delete(argv[1])
        else:
            print ("Nothing to delete.")

    elif argv[0] == 'read':
        if len(argv) > 1:
            r = mongo.read(argv[1])
        else:
            r = mongo.read(None)
        for curr in r:
            print (curr)

    elif argv[0] == 'config':
        # Read and update configuration file
        update_config_file(argv[1])

""" Read and update config file. """
def update_config_file (new_store_name):
    with open(appconfig, 'r') as f:
        config = json.load(f) 
        config['storeName'] = new_store_name
        with open(appconfig, 'w') as f:
            json.dump(config, f)

def get_store_name ():
    with open(appconfig, 'r') as f:
        config = json.load(f) 
        return config['storeName']
