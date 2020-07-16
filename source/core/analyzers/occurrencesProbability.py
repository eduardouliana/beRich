import operator

def analyze(myDic, length):
    
    dic = {}
    
    for number in range(25):
       if myDic.get(number):
           dic[number] = "{:.3f}".format((100 * myDic[number]) / length)

    return dic
    