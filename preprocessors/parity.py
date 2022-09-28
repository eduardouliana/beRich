def insert_parity(draws, conn):
  for draw, numbers in draws.items():
    evens = 0
    odds = 0
    for number in numbers:
      if number %2 == 0:
        evens+=1
      else:
        odds+=1
    conn.execute("UPDATE LOTOFACIL SET EVEN_NUMBERS = " + str(evens) + ", ODD_NUMBERS = " + str(odds) + " WHERE ID = " + str(draw))
  conn.commit()
