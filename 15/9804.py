for a in range(32):
    f = True
    for x in range(32):
        if not((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))):
            f = False
    if f:
        print(a)
        break