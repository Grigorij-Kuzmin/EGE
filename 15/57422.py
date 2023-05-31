for a in range(1, 500):
    f = True
    for x in range(1, 500):
        for y in range(1, 500):
            if not((x >= 12) or (3 * x < y) or (x * y < a)):
                f = False
    if f:
        print(a)
        break