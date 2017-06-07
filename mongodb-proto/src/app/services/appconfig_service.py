"""
+ json: responsible for manipulating JSON.
"""
import json

"""
Name of the configuration file.
"""
APPCONFIG_NAME = 'appconfig.json'

class AppConfigService(object):
    """
    Responsible for retrieve information from the configuration file.
    """
    def set_store_name(self, new_store_name):
        """
        Updates the store name.
        """
        with open(APPCONFIG_NAME, 'r') as config_file_to_read:
            config = json.load(config_file_to_read)
            config['storeName'] = new_store_name
            with open(APPCONFIG_NAME, 'w') as config_file_to_write:
                json.dump(config, config_file_to_write)
    def get_store_name(self):
        """
        Get the current store name in the appconfig.
        """
        with open(APPCONFIG_NAME, 'r') as config_file_to_read:
            config = json.load(config_file_to_read)
            if len(config) > 1:
                return config['storeName']
            else:
                return None
    def get_connection_string(self):
        """
        Get the database connection string from the configuration file.
        """
        with open(APPCONFIG_NAME, 'r') as config_file_to_read:
            config = json.load(config_file_to_read)
            if len(config) > 1:
                return config['connectionString']
            else:
                return None
