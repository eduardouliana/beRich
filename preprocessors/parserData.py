def __insertData(draws, conn):
    for draw, numbers in draws.items():
        conn.execute("INSERT INTO LOTOFACIL (ID, NUMBERS) VALUES (" + str(draw) + ", '" + str(numbers) + "') ON CONFLICT (ID) DO NOTHING")
    conn.commit()

def parser(draws, conn):
    __insertData(draws, conn)