for a in range(1, 132):
    f = True
    for x in range(1, 132):
        if not(((x % 6 == 0) <= (not(x % 10 == 0))) or (x + a > 121)):
            f = False
    if f:
        print(a)
        break
