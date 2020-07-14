import sys
import collections

from core.utils import readFile
from core.analyzers import occurrencesNumberOne

def main():
    allDraws = readFile.read("resource/allDraws.json")

    print("Occurrences of number '1': " + str(occurrencesNumberOne.analyze(allDraws)))

if __name__ == '__main__':
    main()