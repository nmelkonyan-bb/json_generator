import json
from Naked.toolshed.shell import execute_js


def generate_json_from_schema(filePath, outputFilePath):
    arguments = "--filePath=" + filePath + " --outputFilePath=" + outputFilePath
    execute_js('json_generator/json_generator.js', arguments=arguments)


class EventGenerator:
    event = {}

    def __init__(self, json_file_path):
        with open(json_file_path) as file:
            self.event = json.load(file)
            a = self.event

    def get_event(self):
        return self.event

    def set_parameter(self, parameter, value):
        self.event[parameter] = value

    def get_parameter(self, parameter):
        return self.event[parameter]

    def updateTemplate(self, data):
        template = self.event
        for ref in data:
            keys = ref.split(".")
            temp = template
            for key_part in keys[:-1]:
                temp = temp[key_part]
            temp[keys[-1]] = data[ref]
