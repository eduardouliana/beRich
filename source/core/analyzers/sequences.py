def analyze(myList):
    dicResult = {}

    # { "819": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22] }
    def register(first, last):
        indx = str((last + 1) - first)
        if indx not in dicResult: dicResult[indx] = []
        dicResult[indx].append({"draw": draw, "sequence": [first, last]})

    for draw, numbers, in myList.items():
        first = numbers[0]
        last = numbers[0]
        for x in range(len(numbers)):
            if (last + 1) == (numbers[x]): 
                last = numbers[x]
                if x == len(numbers) - 1:
                    register(first, last)
            elif ((last + 1) - first) > 1:
                register(first, last)
                first = numbers[x]
                last = numbers[x]

    return dicResult