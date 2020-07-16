import sys
import collections
import operator

from core.utils import readFile
from core.analyzers import occurrencesAllNumbers, occurrencesProbability

def main():
    allDraws = readFile.read("resource/allDraws.json")
    
    DicOccurrencesAllNumbers = occurrencesAllNumbers.analyze(allDraws)
    print("Occurrence number of all numbers: ", sorted(DicOccurrencesAllNumbers.items(), key=operator.itemgetter(1), reverse=True))
    
    print("");

    DicOccurrencesProbability = occurrencesProbability.analyze(DicOccurrencesAllNumbers, len(allDraws))
    print("Probability: ", sorted(DicOccurrencesProbability.items(), key=operator.itemgetter(1), reverse=True))

if __name__ == '__main__':
    main()