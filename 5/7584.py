x = str
for i in range(1000):
    x = bin(i)[2:]
    if i % 3 == 0:
        x += x[-3:]
    else:
        x += str(bin(3 * (i % 3)))[2:]
    if (int(x, 2)) < 100:
        print(i)