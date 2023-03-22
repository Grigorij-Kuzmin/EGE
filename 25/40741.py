def M(n):
    d = 0
    x = n // 2
    s = 0
    while d != 2:
        if n % x == 0:
            d += 1
            s += x
        x -= 1
        if x == 1:
            return 0
    return s


c = 0
for n in range(10000000, 11000000):
    a = M(n)
    if 0 < a < 10000:
        print(a)
        c += 1
        if c == 5:
            break
