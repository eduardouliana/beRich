import json

def read(path):
    file = open(path, "r")
    return json.load(file)