import itertools
count = 0
ListWord = itertools.product('012345678',repeat=6)
for i in ListWord:
    line = ''.join(i)
    if line.count('4') == 1 and line[0] != '0' and (line.count('1') + line.count('3') + line.count('5') + line.count('7') == 2):
        count += 1
print(count)