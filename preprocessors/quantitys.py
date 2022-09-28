def insert_quantity_of_numbers(draws, conn):
  dic = {}

  for draw, numbers in draws.items():
    for number in numbers:
      dic[number] = dic.get(number, 0) + 1

  query = "INSERT INTO NUMBERS (number, quantity_drawn) VALUES"
  for key, value in dic.items():
    query += " (" + str(key) + ", " + str(value) + "),"
  query = query[:-1]
  conn.execute(query)
  conn.commit()
