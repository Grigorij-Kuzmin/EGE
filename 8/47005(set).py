import itertools

listWord = itertools.product('ПАРАБОЛА', repeat=8)
d = set()
for s in listWord:
    l = ''.join(s)
    if l.count('П') == 1 and l.count('А') == 3 and l.count('Р') == 1 and l.count('Б') == 1 and l.count('О') == 1 and \
            l.count('Л') == 1 and l.count('РП') == 0 and l.count('ПР') == 0 and l.count('ПБ') == 0 and\
            l.count('БП') == 0 and l.count('ПЛ') == 0 and l.count('ЛП') == 0 and l.count('БР') == 0 and\
            l.count('РБ') == 0 and l.count('РЛ') == 0 and l.count('ЛР') == 0 and l.count('БЛ') == 0 and\
            l.count('ЛБ') == 0 and l.count('ПП') == 0 and l.count('РР') == 0 and l.count('ЛЛ') == 0 and\
            l.count('ББ') == 0 and l.count('АА') == 0 and l.count('АО') == 0 and l.count('ОА') == 0:
        d.add(l)
print(len(d))
