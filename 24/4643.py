with open('4643.txt') as f:
    line = f.readline()
    count = 0
    m = 0
    i = 0
    while i != (len(line) - 3):
        if ((line[i] == '1' or line[i] == '2') and (line[i + 1] == '1' or line[i + 1] == '2')) and (line[i + 2] == 'A' or line[i + 2] == 'B'):
            count += 1
            i += 3
        else:
            m = max(count, m)
            count = 0
            i += 1
print(m)