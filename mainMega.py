import sys
import os.path
import operator

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from utils import readFile

def onlyFiveTenItems(dic):
    count = 0
    dic2 = {}
    myList = []
    for draw, number in dic.items():
        count += 1
        if count <= 10:
            dic2[draw] = number
            myList.append(draw)
    
    return myList
        

def orderDic(dic):
    sortedDic = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))

    return onlyFiveTenItems(sortedDic)

def getQuantityOfNumbers(draws):
    dic = {}

    for draw, numbers in draws.items():
        for number in numbers:
            dic[number] = dic.get(number, 0) + 1    

    return orderDic(dic)

def getQuantityOfNumbersThisYear(draws):
    dic = {}

    for draw, numbers in draws.items():
        for number in numbers:
            if int(draw) > 2220:
                dic[number] = dic.get(number, 0) + 1
    
    return orderDic(dic)

def getQuantityOfNumbersLastSixMounths(draws):
    dic = {}

    for draw, numbers in draws.items():
        for number in numbers:
            if int(draw) >= 2275:
                dic[number] = dic.get(number, 0) + 1
    
    return orderDic(dic) 

def getQuantityOfNumbersLastTwoMounths(draws):
    dic = {}

    for draw, numbers in draws.items():
        for number in numbers:
            if int(draw) >= 2315:
                dic[number] = dic.get(number, 0) + 1
    
    return orderDic(dic)

def getQuantityOfNumbersLastTenDraws(draws):
    dic = {}

    for draw, numbers in draws.items():
        for number in numbers:
            if int(draw) >= 2320:
                dic[number] = dic.get(number, 0) + 1
    
    return orderDic(dic) 

#--------------------------------------------------------------------
def getQuantityOfNumbersLastYear2019(draws):
    dic = {}

    for draw, numbers in draws.items():
        for number in numbers:
            if ((int(draw) >= 2111) and (int(draw) <= 2220)):
                dic[number] = dic.get(number, 0) + 1
    
    return orderDic(dic)

def getQuantityOfNumbersLastSixMounths2019(draws):
    dic = {}

    for draw, numbers in draws.items():
        for number in numbers:
            if ((int(draw) >= 2165) and (int(draw) <= 2220)):
                dic[number] = dic.get(number, 0) + 1
    
    return orderDic(dic) 

def getQuantityOfNumbersLastTwoMounths2019(draws):
    dic = {}

    for draw, numbers in draws.items():
        for number in numbers:
            if ((int(draw) >= 2204) and (int(draw) <= 2220)):
                dic[number] = dic.get(number, 0) + 1
    
    return orderDic(dic)

def getQuantityOfNumbersLastTenDraws2019(draws):
    dic = {}

    for draw, numbers in draws.items():
        for number in numbers:
            if ((int(draw) >= 2211) and (int(draw) <= 2220)):
                dic[number] = dic.get(number, 0) + 1
    
    return orderDic(dic)     

def main():    
    allDraws = readFile.read("./resources/mega.json")

    print('Todos:')
    print(getQuantityOfNumbers(allDraws))
    
    print('Este ano:')
    print(getQuantityOfNumbersThisYear(allDraws))

    print('Últimos 6 meses:')
    print(getQuantityOfNumbersLastSixMounths(allDraws))

    print('Últimos 2 meses:')
    print(getQuantityOfNumbersLastTwoMounths(allDraws))

    print('Últimos 10 sorteios:')
    print(getQuantityOfNumbersLastTenDraws(allDraws))

    print('Ano 2019:')
    print(getQuantityOfNumbersLastYear2019(allDraws))

    print('Últimos 6 meses Ano 2019:')
    print(getQuantityOfNumbersLastSixMounths2019(allDraws))

    print('Últimos 2 meses Ano 2019:')
    print(getQuantityOfNumbersLastTwoMounths2019(allDraws))

    print('Últimos 10 sorteios Ano 2019:')
    print(getQuantityOfNumbersLastTenDraws2019(allDraws))

if __name__ == '__main__':
    main()