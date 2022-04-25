def adjust(s):
    s = s.replace('01,', '1,')
    s = s.replace('02,', '2,')
    s = s.replace('03,', '3,')
    s = s.replace('04,', '4,')
    s = s.replace('05,', '5,')
    s = s.replace('06,', '6,')
    s = s.replace('07,', '7,')
    s = s.replace('08,', '8,')
    s = s.replace('09,', '9,')

    s = s.replace('"000', '"')
    s = s.replace('"00', '"')
    s = s.replace('"0', '"')

    return s

f = open("resources/mega.json", "r")
f2 = open("resources/mega2.json", "w")

for x in f:
  f2.write(adjust(x))
