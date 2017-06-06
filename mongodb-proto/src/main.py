# -*- coding: utf-8 -*-

import sys
import json
from app.services.mongo_service import MongoService
from datetime import datetime

appconfig = 'config\appconfig.json'

def main(argv):
    mongoService = MongoService("CasasBahia")

    if argv[0] == 'insert':
        # Insert something
        mongoService.insert({"author": "Vivi", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.utcnow()})

    elif argv[0] == 'update':
        # Update data
        pass

    elif argv[0] == 'delete':
        # Delete something
        mongoService.delete('aa')

    elif argv[0] == 'select':
        r = mongoService.get({"author": "Vivi"})
        print (r['text'])

    elif argv[0] == 'config':
        # Read and update configuration file
        update_config_file(argv[1])

""" Read and update config file. """
def update_config_file (new_store_name):
    with open('appconfig.json', 'r') as f:
        config = json.load(f) 
        config['storeName'] = argv[1]
        with open('appconfig.json', 'w') as f:
            json.dump(config, f)

if __name__ == "__main__":
    main(sys.argv[1:])