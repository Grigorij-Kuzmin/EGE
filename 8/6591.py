import itertools
listWords = itertools.product('0123456', repeat=5)
count = 0
for s in listWords:
    line = ''.join(s)
    c = line.count('2') * 2 + line.count('4') * 4 + line.count('6') * 6
    n = line.count('1') + line.count('3') * 3 + line.count('5') * 5
    if line[0] != '0' and line.count('6') == 1 and n > c:
        count += 1
print(count)