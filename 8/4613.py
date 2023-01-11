import itertools
listword = itertools.product('012345678', repeat= 5)
count = 0
for s in listword:
    line = ''.join(s)
    if line[0] != '1' and line[0] != '3' and line[0] != '5' and line[0] != '7' and line[4] != '1' and line[4] != '8' and line.count('3') <= 1 and line[0] != '0':
        count += 1
print(count)