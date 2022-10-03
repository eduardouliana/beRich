from itertools import combinations

def combination_util(arr, data, start, end, index, r, result):
  if (index == r):
    result.append(data[:])
    return;

  i = start;
  while(i <= end and end - i + 1 >= r - index):
    data[index] = arr[i];
    combination_util(arr, data, i + 1, end, index + 1, r, result);
    i += 1;

def feed_numbers_with_single_combination(draws, conn):
  dic = {}
  for draw, numbers in draws.items():
    for number in numbers:
      dic.setdefault(number, {})
      for validate_number in numbers:
        if validate_number == number:
            continue
        dic[number][validate_number] = dic[number].get(validate_number, 0) + 1

  query = "UPDATE NUMBERS SET combinations = \"{combinations}\" where number = {number}"
  for key, value in dic.items():
    conn.execute(query.format(number=key, combinations=value))
  conn.commit()

# 1 - gerar todas as combinações de 1-25 com a quantidade de numeros informados
def generate_combinations(draws, conn, quantity_numbers):
  ary = list(range(1, 25))
  n = len(ary)
  data = [0]*quantity_numbers;
  result = []

  #combinationUtil(ary, data, 0, n - 1, 0, quantity_numbers, result);
  result = combinations(ary, quantity_numbers)

  for combination in result:
    ocurrences = _find_combinations(draws, combination)
    query = "INSERT INTO COMBINATIONS (COMBINATION, OCCURRENCES, QUANTITY) VALUES (\"{combination}\", {ocurrences}, {quantity})"
    conn.execute(query.format(combination=combination, ocurrences=ocurrences, quantity=quantity_numbers))
  conn.commit();

# 2 - procurar quantas vezes a combinação aparceu nos resultados
def _find_combinations(draws, combination):
  count = 0
  for draw, numbers in draws.items(): # cada linha
    set_numbers = set(numbers)
    if set(combination).issubset(set_numbers):
      count += 1;
  return count
