import itertools as it
import json

DEFAULT_DRAW_LENGHT = 15
MAX_DRAW_NUMBER = 25
FILE_PATH = "all_combinations_15.json"

def save_to_file(content):
  file_data = open(FILE_PATH, "w")
  json.dump(content, file_data)

def main():
  items = range(1, MAX_DRAW_NUMBER + 1)
  all_combinations = list(it.combinations(items, DEFAULT_DRAW_LENGHT))

  combinations = {}
  for combination in all_combinations:
    key = ':'.join(str(n) for n in combination)
    combinations[key] = combination

  save_to_file(combinations)

if __name__ == '__main__':
  main()
