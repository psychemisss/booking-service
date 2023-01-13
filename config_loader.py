import json


class ConfigLoader:
    def __init__(self, config_file: str = 'config.json'):
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
