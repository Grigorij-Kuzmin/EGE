s = str
for n in range(1001, 10000):
    s = bin(n)[2:]
    s = s.replace('0', '2')
    s = s.replace('1', '0')
    s = s.replace('2', '1')
    x = s.find('1')
    if x != -1:
        s = s[x:]
    if n - int(s, 2) == 979:
        print(n)
        break