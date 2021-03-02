import json
import random
import os
from app.data import messages


class JsonService(object):
    file_path = None
    key = None

    def __init__(self, file_path, key=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_path = file_path
        self.key = key

    def readJsonFile(self):
        with open(os.getcwd() + self.file_path) as json_file:
            return json.load(json_file)

    def getJsonKeys(self):
        data = self.readJsonFile()
        return data.keys()

    def getJsonValue(self):
        data = self.readJsonFile()
        if self.key not in self.getJsonKeys():
            raise Exception(messages.input_not_match)
        return data[self.key]

    def getRandomValue(self):
        return random.choice(self.getJsonValue())
