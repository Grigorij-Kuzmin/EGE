m = 0
b = []
with open('24_7600.txt') as f:
    line = (f.readline())
    line = line.replace('Q', '1')
    line = line.replace('R', '1')
    line = line.replace('S', '1')
    b = line.split('11')
    for i in range(len(b)):
        if i == 0 or i == len(b) - 1:
            m = max(m, len(b[i]) + 1)
        else:
            m = max(m, len(b[i]) + 2)
print(m)
