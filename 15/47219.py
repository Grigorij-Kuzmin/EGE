for a in range(1, 100):
    f = True
    for x in range(1, 100):
        if not((x % 2 == 0) <= (x % 3 != 0) or (x + a >= 100)):
            f = False
    if f:
        print(a)
        break