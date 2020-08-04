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
            if (x == len(numberList) - 1):
                register(first, last)

    return sequences

def __extractGroups(sequences):

    group  = []
    for sequence in sequences:
        if len(sequence) == 1:
            group.append(1)
        else:
            group.append(sequence[1] - sequence[0] + 1)
    return group

def __insertSequencesAndGroups(draws, conn):
    for draw, numbers in draws.items():
        sequences = __extractSequences(numbers)
        groups = __extractGroups(sequences)
        conn.execute("UPDATE LOTOFACIL SET SEQUENCES = '" + str(sequences) + "', GROUPS = '" + str(groups) + "' where id = " + str(draw))
    conn.commit()

def parser(draws, conn):
    __insertData(draws, conn)
    __insertSequencesAndGroups(draws, conn)