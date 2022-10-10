import sys
sys.path.append('../')

from database.postgresql import PostgreSQL
import json

def _load_all_draws():
  FILE_PATH = '../resources/jogos_sorteados.json'
  file = open(FILE_PATH, "r")
  return json.load(file)

def main():
  draws = _load_all_draws()

  db = PostgreSQL()
  for key, value in draws.items():
    db.set_sorted(key, ':'.join(str(n) for n in value))

  del db
if __name__ == '__main__':
  main()
