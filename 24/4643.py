with open('4643.txt') as f:
    line = f.readline()
    count = 1
    m = 0
    for i in range(len(line) - 3):
        if ((line[i] == '1' or line[i] == '2') and (line[i + 1] == '1' or line[i + 1] == '2')) and (line[i + 3] == 'A' or line[i + 3] == 'B'):
            count += 1
        else:
            m = max(count, m)
            count = 1
print(m)