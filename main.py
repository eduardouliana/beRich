import sys
import os.path

sys.path.append(
  os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from utils import readFile
from core import preprocessor
from database import connection

def main():
  all_draws = readFile.read("./resources/allDraws.json")

  conn = connection.connectDB('./resources/database.db')

  preprocessor.process(all_draws, conn)

if __name__ == '__main__':
  main()
