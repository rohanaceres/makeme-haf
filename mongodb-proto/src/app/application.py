"""
+ mongo_service: responsible for providing mongo access operations.
+ mock_amazon: mocks an instance of Amazon store.
+ mock_bestbuy: mocks an instance of BestBuy store.
"""
from app.services import mongo_service
from app.services import appconfig_service
from app.mocking.database_mocker import mock_amazon, mock_bestbuy

def go_for_it_girl(argv):
    """
    Performs an action accordingly to the first argument received from command line.
    """
    appconfig = appconfig_service.AppConfigService()
    mongo = mongo_service.MongoService(
        appconfig.get_store_name(),
        appconfig.get_connection_string())

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
        for current_document in documents:
            print(current_document)
    elif argv[0] == 'config':
        # Read and update configuration file
        appconfig.set_store_name(argv[1])

