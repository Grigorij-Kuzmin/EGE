count = 0
m = 0
with open('37159.txt') as f:
    line = f.readline()
    for i in range(len(line) - 1):
        if (line[i] != 'a' and line[i + 1] != 'd') or (line[i] != 'd' and line[i + 1] != 'a'):
            count += 1
            m = max(m, count)
        else:
            m = max(m, count)
            count = 0
print(m)