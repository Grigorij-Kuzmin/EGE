count = 0
import itertools
listWord = itertools.product('012345678', repeat=7)
for s in listWord:
    line = ''.join(s)
    if (line.count('6') == 1) and (line[0] != '0') and (line.count('1') + line.count('3') + line.count('5') + line.count('7') == 2):
        count += 1
print(count)