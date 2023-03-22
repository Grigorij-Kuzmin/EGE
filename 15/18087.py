for a in range(1, 100):
    F = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not((y + 2*x < a) or (x > 15) or (y > 30)):
                F = False
    if F:
        print(a)
        break