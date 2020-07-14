def analyze(myList):
    count = 0

    for draw, numbers in myList.items():
        if 1 in numbers:
            count += 1
    
    return count