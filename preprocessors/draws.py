import itertools as it
import random

DEFAULT_DRAW_LENGHT = 15
MAX_DRAW_NUMBER = 25

def as_string(numbers):
  return ','.join(str(x) for x in numbers)

def extract_sequences(number_list):
  def register(first, last):
    if first == last:
      sequences.append([first])
    else:
      sequences.append([first, last])

  first = int(number_list[0])
  last = int(number_list[0])
  sequences = []

  for x in range(len(number_list)):
    if (last + 1) == int(number_list[x]):
      last = int(number_list[x])
      if x == len(number_list) - 1:
        register(first, last)
    elif ((last + 1) - first) > 0:
      if (x > 0): # Skip first execution
        register(first, last)
      first = int(number_list[x])
      last = int(number_list[x])
      if (x == len(number_list) - 1):
        register(first, last)

  return sequences

def extract_groups(sequences):
  group  = []
  for sequence in sequences:
    if len(sequence) == 1:
      group.append(1)
    else:
      group.append(sequence[1] - sequence[0] + 1)
  return group

class Draw():
  def __init__(self, numbers):
    self.numbers = numbers
    self.sorted_id = None
    self.sequences = extract_sequences(numbers)
    self.groups = extract_groups(self.sequences)

  def set_sorted(self, draw_id):
    self.sorted_id = draw_id

  def as_string(self):
    return as_string(self.numbers)

  def contains(self, numbers):
    for number in numbers:
      if number not in self.numbers:
        return False

    return True

  def print_report(self):
    is_sorted = ''
    if self.sorted_id:
      is_sorted = ' - Já sorteado'

    print(f'---------------------------------------------')
    print(f' {self.as_string()} {is_sorted}  ')
    print(f' Sequencias: {self.sequences}')
    print(f' Grupos: {self.groups}')

class Draws():
  def __init__(self, draw_lenght = DEFAULT_DRAW_LENGHT):
    self._bet_length = draw_lenght
    self._draws = self._generate_draws(draw_lenght)
    self._sorted_draws = []

  def iter_draws(self):
    for key, value in self._draws.items():
      yield [key, value]

  def set_sorted(self, draw_id, draw_numbers):
    str_numbers = as_string(draw_numbers)

    self._draws[str_numbers].set_sorted(draw_id)
    self._sorted_draws.append(str_numbers)

  def is_sorted(self, numbers):
    return numbers in self._sorted_draws

  def _generate_draws(self, draw_length):
    possible_numbers = range(1, MAX_DRAW_NUMBER + 1)
    combinations = self._all_possible_combinations(draw_length, possible_numbers)

    return self._build_draws(combinations)

  def _build_draws(self, combinations):
    draws = {}

    for combinantion in combinations:
      draw = Draw(combinantion)
      draws[draw.as_string()] = draw

    return draws

  def _all_possible_combinations(self, qnt, items):
    return list(it.combinations(items, qnt))

  def predict(self, qnt, containing_numbers):
    games = []
    while len(games) < qnt:
      game = random.sample(containing_numbers, k=self._bet_length)
      game.sort()

      game = as_string(game)

      if game in games:
        continue

      if self.is_sorted(game):
        continue

      games.append(game)

    for game in games:
      self._draws[game].print_report()
