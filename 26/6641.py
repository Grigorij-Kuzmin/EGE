a = []
b = []
x = 0
count = 0
with open('26_6641.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line.find('S') != -1:
            a.append(line[:-2])
        else:
            b.append(line[:-2])
        a.sort()
        b.sort()
        m = max((len(a), len(b)))
    for i in range(m):
        while x < 395200:
            if int(a[i]) >= int(b[i]):
                count += 1
                x += int(a[i])
            else:
                x += int(b[i])
print(count, x - 395200)