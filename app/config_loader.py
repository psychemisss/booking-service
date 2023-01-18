import json
import os

def find_config_file():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file == 'config.json':
                return os.path.join(root, file)

class ConfigLoader:
    def __init__(self, config_file: str = find_config_file()):
        self.config_file = config_file

    @property
    def config(self):
        with open(self.config_file) as f:
            return json.load(f)

    def get_keys(self):
        return self.config.keys()

    def get_keys_specified(self, key):
        return self.config[key].keys()

    def get_item(self, key: str):
        return self.config[key]

    def get_item_specified(self, key: str, item: str):
        return self.config[key][item]
