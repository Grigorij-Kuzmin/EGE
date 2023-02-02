import itertools

listWord = itertools.product('ПАРАБОЛА', repeat=8)
count = 0
for s in listWord:
    line = ''.join(s)
    if line.count('П') == 1 and line.count('А') == 3 and line.count('Р') == 1 and line.count('Б') == 1 and line.count('О') == 1 and line.count('Л') == 1 and line.count('РП') == 0 and line.count('ПР') == 0 and line.count('ПБ') == 0 and line.count('БП') == 0 and line.count('ПЛ') == 0 and line.count('ЛП') == 0 and line.count('БР') == 0 and line.count('РБ') == 0 and line.count('РЛ') == 0 and line.count('ЛР') == 0 and line.count('БЛ') == 0 and line.count('ЛБ') == 0 and line.count('ПП') == 0 and line.count('РР') == 0 and line.count('ЛЛ') == 0 and line.count('ББ') == 0 and line.count('АА') == 0 and line.count('ОО') == 0 and line.count('АО') == 0 and line.count('ОА') == 0:
        count += 1
        print(line)
print(count)