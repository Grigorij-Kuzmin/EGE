with open('47021.txt') as f:
    line = f.readline()
    count = 0
    a = []
    a = line.split('A')
    for i in range(len(a)):
        if (a[i].count('B') == 0) and (len(a[i]) >= 8):
            count += 1
print(count)
