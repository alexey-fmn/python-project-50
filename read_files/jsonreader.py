import json


class JsonReader:

    @staticmethod
    def read(filepath):
        with open(filepath) as json_file:
            return json.load(json_file)

    @staticmethod
    def show(filepath):
        data = JsonReader.read(filepath)
        return json.dumps(data, indent=4, sort_keys=True)
