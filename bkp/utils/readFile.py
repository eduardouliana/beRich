import json

def read(path):
  file_data = open(path, "r")

  return json.load(file_data)
