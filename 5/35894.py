x = str
for n in range(105, 200):
    x = bin(n)[2:]
    for i in range(3):
        if x.count('1') > x.count('0'):
            x += '0'
        if x.count('1') < x.count('0'):
            x += '1'
        else:
            x += x[-1]
    if int(x, 2) % 4 == 0:
        print(n)
        break
