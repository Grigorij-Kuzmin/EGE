for n in range(3, 100):
    x = '3' + n * '5'
    while ('25' in x) or ('355' in x) or ('555' in x):
        if '25' in x:
            x = x.replace('25', '3', 1)
        if '355' in x:
            x = x.replace('355', '52', 1)
        if '555' in x:
            x = x.replace('555', '23', 1)
    s = 0
    for i in range(len(x)):
        s += int(x[i])
    if s == 27:
        print(n)
        break