r = 0
n = 0
for n in range(1, 1000):
    r = 0
    count = 0
    count1 = 0
    x = bin(n)[2:]
    count = x[1::2].count('1')
    count1 = x[0::2].count('0')
    r = abs(count - count1)
    if r == 4:
        print(n)
        break