import json
import random
import os


class JsonService(object):
    file_path = None
    json_content = None
    input_not_match_msg = ''

    def __init__(self, input_not_match_msg, file_path, json_content=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_not_match_msg = input_not_match_msg
        self.file_path = file_path
        self.json_content = json_content
        self.readJsonContent()

    def readJsonFile(self):
        with open(os.getcwd() + self.file_path) as json_file:
            return json.load(json_file)

    def readJsonContent(self):
        self.json_content = self.readJsonFile()

    def getJsonKeys(self):
        if self.json_content is None:
            return None
        return self.json_content.keys()

    def getJsonValue(self, key):
        data = self.json_content
        if data is None or key not in self.getJsonKeys():
            raise Exception(self.input_not_match_msg)
        return data[key]

    def getRandomValueByKey(self, key):
        return random.choice(self.getJsonValue(key))
