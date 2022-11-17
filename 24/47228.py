with open('47228.txt') as f:
    line = f.readline()
    count = 0
    m = 0
    i = 0
    while i < len(line):
        if (line[i] == 'C' or line[i] == 'D' or line[i] == 'F') and (line[i + 1] == 'A' or line[i + 1] == 'O'):
            count += 1
            m = max(count, m)
            i += 2
        else:
            count = 0
            i += 1
print(m)

