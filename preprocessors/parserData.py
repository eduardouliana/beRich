import pprint
import time

def combinationUtil(arr, data, start, end, index, r, result): 
    if (index == r): 
        result.append(data[:])
        return; 

    i = start;  
    while(i <= end and end - i + 1 >= r - index): 
        data[index] = arr[i]; 
        combinationUtil(arr, data, i + 1, end, index + 1, r, result); 
        i += 1;


def __insertData(draws, conn):
    query = 'INSERT INTO LOTOFACIL (ID, NUMBERS) VALUES'
    for draw, numbers in draws.items():
        query += " (" + str(draw) + ", '" + str(numbers) + "'),"
    query = query[:-1] # More efficient to remove the last comma, instead of comparing whether it is the last one at each interaction
    query += " ON CONFLICT (ID) DO NOTHING"
    conn.execute(query)
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
        conn.execute("UPDATE LOTOFACIL SET SEQUENCES = '" + str(sequences) + "', GROUPS = '" + str(groups) + "' WHERE ID = " + str(draw))
    conn.commit()

def __insertParity(draws, conn):
    for draw, numbers in draws.items():
        evenNumbers = 0
        oddNumbers = 0        
        for number in numbers:
            if number %2 == 0:
                evenNumbers+=1
            else:
                oddNumbers+=1
        conn.execute("UPDATE LOTOFACIL SET EVEN_NUMBERS = " + str(evenNumbers) + ", ODD_NUMBERS = " + str(oddNumbers) + " WHERE ID = " + str(draw))
    conn.commit()

def __insertQuantityOfNumbers(draws, conn):
    dic = {}

    for draw, numbers in draws.items():
        for number in numbers:
            dic[number] = dic.get(number, 0) + 1
    
    #{1: 1277, 2: 1274, 3: 1255, 5: 1235, 7: 1203, 8: 1169, 11: 1260, 12: 1220, 14: 1239, 17: 1225, 19: 1235, 21: 1217, 22: 1238, 23: 1237, 4: 1251, 9: 1211, 13: 1272, 15: 1220, 16: 1183, 18: 1227, 24: 1266, 
    #6: 1193, 25: 1245, 10: 1233, 20: 1225}

    query = "INSERT INTO NUMBERS (number, quantity_drawn) VALUES"
    for key, value in dic.items():
        query += " (" + str(key) + ", " + str(value) + "),"
    query = query[:-1]
    conn.execute(query)
    conn.commit()

def __feedNumbersWithSingleCombination(draws, conn):
    dic = {}       
    for draw, numbers in draws.items():
        for number in numbers:
            dic.setdefault(number, {})
            for validateNumber in numbers:
                if validateNumber == number:
                    continue
                dic[number][validateNumber] = dic[number].get(validateNumber, 0) + 1                 
    
    query = "UPDATE NUMBERS SET combinations = \"{combinations}\" where number = {number}"
    for key, value in dic.items():
        conn.execute(query.format(number=key, combinations=value))
    conn.commit()

# 1 - gerar todas as combinações de 1-25 com a quantidade de numeros informados
def __generateCombinations(draws, conn, quantity_numbers):
    ary = list(range(1, 25))
    n = len(ary)
    data = [0]*quantity_numbers; 
    result = []

    combinationUtil(ary, data, 0, n - 1, 0, quantity_numbers, result); 
    
    for combination in result:
       ocurrences = __findCombinations(draws, combination) 
       query = "INSERT INTO COMBINATIONS (COMBINATION, OCCURRENCES, QUANTITY) VALUES (\"{combination}\", {ocurrences}, {quantity})"
       conn.execute(query.format(combination=combination, ocurrences=ocurrences, quantity=quantity_numbers))
    conn.commit();       

# 2 - procurar quantas vezes a combinação aparceu nos resultados 
def __findCombinations(draws, combination):
    count = 0
    for draw, numbers in draws.items(): # cada linha
        set_numbers = set(numbers)
        if set(combination).issubset(set_numbers):
            count += 1;    
    return count

def parser(draws, conn):
    ini = time.time()
    print(ini)

    __insertData(draws, conn)
    lap1 = time.time()
    print("Insert data", lap1 - ini)

    __insertSequencesAndGroups(draws, conn)
    lap2 = time.time()
    print("Sequences", lap2 - lap1)

    __insertParity(draws, conn)
    lap3 = time.time()
    print("Parity", lap3 - lap2)

    __insertQuantityOfNumbers(draws, conn)
    lap4 = time.time()
    print("Quantity of numbers", lap4 - lap3)

    __feedNumbersWithSingleCombination(draws, conn)
    lap5 = time.time()
    print("Number with single combinations", lap5 - lap4)

    for n in range(1,6):
        lapx = time.time() 
        __generateCombinations(draws,conn, n)
        lapy = time.time()
        print("Occurences of combinations", lapy - lapx)    
    lap6 = time.time()
    print("End of occurences of combinations", lap6 - lap5)        