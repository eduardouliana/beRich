def insert_data(draws, conn):
  query = 'INSERT INTO LOTOFACIL (ID, NUMBERS) VALUES'
  for draw, numbers in draws.items():
    query += " (" + str(draw) + ", '" + str(numbers) + "'),"
  query = query[:-1]
  query += " ON CONFLICT (ID) DO NOTHING"
  conn.execute(query)
  conn.commit()
