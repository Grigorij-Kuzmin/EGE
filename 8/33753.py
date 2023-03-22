import itertools
listWord = itertools.product('АНДРЕЙ',  repeat=6)
count = 0
for s in listWord:
    line = ''.join(s)
    if line.count('А') >= 1 and line.count('Й') <= 1:
        count += 1
print(count)