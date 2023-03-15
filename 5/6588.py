x = str
for n in range(100):
    x = bin(n)[2:]
    x = x.replace('1', '2')
    x = x.replace('0', '3')
    x = x.replace('2', '0')
    x = x.replace('3', '1')
    x = '1' + x
    if x.count('1') % 2 == 0:
        x = x + '0'
    else:
        x = x + '1'
    if int(x, 2) > 180:
        print(n)
        break