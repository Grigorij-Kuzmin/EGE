with open('27699.txt') as f:
    line = f.readline()
    x = 0
    str = ''
    while x != -1:
        str += 'L'
        x = line.find(str)
        if x != -1:
            str += 'D'
            x = line.find(str)
            if x != -1:
                str += 'R'
                x = line.find(str)
print(len(str) - 1)