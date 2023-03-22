for a in range(1, 2048):
    f = True
    for x in range(1, 2048):
        if not((x & 1097 == 0) <= ((x & 2047 != 0) <= (x & a != 0))):
            f = False
    if f:
        print(a)
        break