import sys
import time
import os.path

sys.path.append(
  os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from preprocessors.parser_data import insert_data
from preprocessors.combinations import feed_numbers_with_single_combination, generate_combinations
from preprocessors.groups_sequences import insert_sequences_and_groups
from preprocessors.parity import insert_parity
from preprocessors.quantitys import insert_quantity_of_numbers

def process(draws, conn):
  ini = time.time()
  print(ini)

  insert_data(draws, conn)
  lap1 = time.time()
  print("Insert data", lap1 - ini)

  insert_sequences_and_groups(draws, conn)
  lap2 = time.time()
  print("Sequences", lap2 - lap1)

  insert_parity(draws, conn)
  lap3 = time.time()
  print("Parity", lap3 - lap2)

  insert_quantity_of_numbers(draws, conn)
  lap4 = time.time()
  print("Quantity of numbers", lap4 - lap3)

  feed_numbers_with_single_combination(draws, conn)
  lap5 = time.time()
  print("Number with single combinations", lap5 - lap4)

  for n in range(1,6):
    lapx = time.time()
    generate_combinations(draws,conn, n)
    lapy = time.time()
    print("Occurences of combinations", lapy - lapx)
  lap6 = time.time()
  print("End of occurences of combinations", lap6 - lap5)
