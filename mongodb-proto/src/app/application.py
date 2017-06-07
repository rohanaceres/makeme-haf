"""
+ json: responsible for manipulating JSON.
+ mongo_service: responsible for providing mongo access operations.
+ mock_amazon: mocks an instance of Amazon store.
+ mock_bestbuy: mocks an instance of BestBuy store.
"""
import json
from app.services import mongo_service
from app.mocking.database_mocker import mock_amazon, mock_bestbuy

"""
Name of the configuration file.
"""
APPCONFIG_NAME = 'appconfig.json'

def go_for_it_girl(argv):
    """
    Performs an action accordingly to the first argument received from command line.
    """
    mongo = mongo_service.MongoService(__get_store_name())

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
            mongo.delete(argv[1])
        else:
            print("Nothing to delete.")
    elif argv[0] == 'read':
        if len(argv) > 1:
            documents = mongo.read(argv[1])
        else:
            documents = mongo.read(None)
        for curr in documents:
            print(curr)
    elif argv[0] == 'config':
        # Read and update configuration file
        __update_config_file(argv[1])

def __update_config_file(new_store_name):
    """
    Read and update config file.
    """
    with open(APPCONFIG_NAME, 'r') as config_file_to_read:
        config = json.load(config_file_to_read)
        config['storeName'] = new_store_name
        with open(APPCONFIG_NAME, 'w') as config_file_to_write:
            json.dump(config, config_file_to_write)
def __get_store_name():
    """
    Get the current store name in the appconfig.
    """
    with open(APPCONFIG_NAME, 'r') as config_file_to_read:
        config = json.load(config_file_to_read)
        if len(config) > 1:
            return config['storeName']
        else:
            return None
