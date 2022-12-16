import itertools

listWords = itertools.product('01234567', repeat=5)
count = 0
for s in listWords:
    line = ''.join(s)
    if line.count('6') == 1 and line.count('16') == 0 and line.count('36') == 0 and line.count('56') == 0 and line.count('76') == 0 and\
            line.count('61') == 0 and line.count('63') == 0 and line.count('65') == 0 and line.count('67') == 0 and line[0] != '0':
        count += 1
print(count)