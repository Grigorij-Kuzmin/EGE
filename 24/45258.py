with open('45258.txt') as f:
    line = f.readline()
    count = 0
    m = 0
    i = 0
    while i < len(line):
        if (line[i] == 'A' or line[i] == 'C') and (line[i + 1] == 'B'):
            count += 1
            i += 2
        else:
            m = max(m, count)
            count = 0
            i += 1
print(m)