import sys
import collections
import operator

from core.utils import readFile
from core.analyzers import occurrencesAllNumbers, occurrencesProbability, sequences

def main():
    allDraws = readFile.read("resource/allDraws.json")
    
    print(allDraws)

    DicOccurrencesAllNumbers = occurrencesAllNumbers.analyze(allDraws)
    print("Occurrence number of all numbers: ", sorted(DicOccurrencesAllNumbers.items(), key=operator.itemgetter(1), reverse=True))
    
    print("");

    DicOccurrencesProbability = occurrencesProbability.analyze(DicOccurrencesAllNumbers, len(allDraws))
    print("Probability: ", sorted(DicOccurrencesProbability.items(), key=operator.itemgetter(1), reverse=True))

  #  DicSequences = sequences.analyze(allDraws)
  #  print("Sequences", sorted(DicSequences.items(), key=operator.itemgetter(0)))
  #  print("Quantity Sequences")
  #  for seq, nums in DicSequences.items():
  #      print(seq, ": ", str(len(nums)))

   # conjuntos = {}

   # for seq, nums in DicSequences.items():
   ##     for num in nums:
   #         if num["draw"] not in conjuntos: conjuntos[num["draw"]] = []
   #         conjuntos[num["draw"]].append({seq: num["sequence"]})

   # print(conjuntos)
if __name__ == '__main__':
    main()