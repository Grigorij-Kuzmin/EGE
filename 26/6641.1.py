a = []
s = 0
c = 0
b = []
with open('26_6641.txt') as f:
    lines = f.readlines()
    for line in lines:
        items = line.split()
        a.append([int(items[0])], [items[1]])
    a.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(a)):
        if s < 395200:
            s += a[i][0]
            c += 1
    b = a[:c]
    a = a[c:]
    a.sort(key=lambda x: (x[1], x[0]))
    b.sort(key=lambda x: (x[1], x[0]))
    for i in range(len(a)):
