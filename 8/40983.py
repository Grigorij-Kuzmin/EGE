import itertools
d = set()
listWord = itertools.product('ГЕОРГИЙ', repeat=7)
for s in listWord:
    l = ''.join(s)
    if l.count('Г') == 2 and l.count('Е') == 1 and l.count('О') == 1 and l.count('Р') == 1 and l.count('И') == 1 and l.count('Й') == 1 and l.count('ГГ') == 0:
        d.add(l)
print(len(d))