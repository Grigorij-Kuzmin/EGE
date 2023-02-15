m = 0
with open('40740.txt') as f:
    line = f.readline()
    while line.find('A') != -1:
        str = line[:(line.find(('А')))]
        line = line[(line.find(('A')) + 1):]
        if str.count('E') >= 3:
            m = max(m, len(str))
print(m)

