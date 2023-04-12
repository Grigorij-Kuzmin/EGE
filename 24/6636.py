with open('24_6636.txt') as f:
    line = f.readline()
    count = 0
    m = 0
    i = 0
    while i != len(line) - 1:
        if (int(line[i]) % 2 == 0) and (int(line[i + 1]) % 2 != 0):
            count += 1
            m = max(m, count)
            i += 2
        else:
            count = 0
            i += 1
print(m)