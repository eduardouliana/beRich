def __insertData(draws, conn):
    for draw, numbers in draws.items():
        conn.execute("INSERT INTO LOTOFACIL (ID, NUMBERS) VALUES (" + str(draw) + ", '" + str(numbers) + "') ON CONFLICT (ID) DO NOTHING")
    conn.commit()

def __toList(str):
    return str.strip('][').split(', ')


def __extractSequences(numberList):
    def register(first, last):
        if first == last:
            sequences.append([first])
        else:
            sequences.append([first, last])    

    first = int(numberList[0])
    last = int(numberList[0])
    sequences = []

    for x in range(len(numberList)):
        if (last + 1) == int(numberList[x]):
            last = int(numberList[x])
            if x == len(numberList) - 1:
                register(first, last)
        elif ((last + 1) - first) > 0:
            if (x > 0): # Skip first execution
                register(first, last)
            first = int(numberList[x])
            last = int(numberList[x])

    return sequences

def __insertSequences(draws, conn):
    for draw, numbers in draws.items():
        sequences = __extractSequences(numbers)
        conn.execute("UPDATE LOTOFACIL SET SEQUENCES = '" + str(sequences) + "' where id = " + str(draw))
    conn.commit()

def parser(draws, conn):
    __insertData(draws, conn)
    __insertSequences(draws, conn)