import sys
import os.path

sys.path.append(
  os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from utils import readFile
from preprocessors.draws import Draws

def set_sorted_draws(draws):
  all_draws = readFile.read("./resources/allDraws.json")

  for draw_id, draw_numbers in all_draws.items():
    draws.set_sorted(draw_id, draw_numbers)

def print_report(draws):
  for key, draw in draws.iter_draws():
    if draw.sorted_id:
      draw.print_report()

def main():
  draws = Draws()
  print('Draws generated!')
  set_sorted_draws(draws)
  print('Sorted draws setted')
  draws.predict(10, [1,2,3,4,5,6,8,9,10,11,13,14,15,18,19,20,21,22,23,24])

if __name__ == '__main__':
  main()
