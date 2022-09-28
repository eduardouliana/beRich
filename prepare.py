import sys
import os.path
import itertools as it

sys.path.append(
  os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from utils import readFile
from core import preprocessor
from database import connection

def generate_all_possible_draws(qnt):
  return list(it.combinations(range(1,26), qnt))

def main():
  #all_draws = readFile.read("./resources/allDraws.json")

  conn = connection.connect_db('./resources/database.db')

  connection.prepare(conn)

  all_possible_draws = generate_all_possible_draws(15)
  preprocessor.process(all_possible_draws, conn)
  print(len(all_possible_draws))

if __name__ == '__main__':
  main()
