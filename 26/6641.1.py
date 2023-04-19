a = []
s = 0
c = 0
b = []
count = 0
with open('26_6641.txt') as f:
    lines = f.readlines()
    for line in lines:
        items = line.split()
        a.append([int(items[0]), items[1]])
    a.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(a)):
        if s + a[i][0] < 395200:
            s += a[i][0]
            c += 1
    b = a[:c]
    a = a[c:]
    a.sort(key=lambda x: (x[1], x[0]))
    b.sort(key=lambda x: (x[1], x[0]))
    i = 0
    while i <= len(a) and i <= len(b):
        if s + a[(len(b) - i)][0] - b[i][0] < 395200:
            a[i][0] = b[(len(b) - i)]
            s += a[(len(b) - i)][0] - b[i][0]
            count += 1
        i += 1
print(count, s)


