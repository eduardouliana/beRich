import json

def read(path):
    file = open(path, "r")
    myList = json.load(file)

    return myList