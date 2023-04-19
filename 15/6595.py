for a in range(1, 1000):
    f = True
    for x in range(1, 1000):
        if not(((x % 3 == 0) <= (not(x % 2 == 0))) or (x - a >= 4)):
            f = False
    if f:
        print(a)