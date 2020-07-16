import operator

def analyze(myList):
    
    dic = {}

    for draw, numbers in myList.items():
        for number in range(25):
            if number in numbers:
                if dic.get(number):
                    dic[number] += 1
                else:
                    dic[number] = 1

    return dic
        