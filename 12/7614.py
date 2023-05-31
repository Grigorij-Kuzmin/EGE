for n in range(4, 100):
    str = '3' + n * '5'
    while '25' in str or '355' in str or '555' in str:
        if '25' in str:
            str = str.replace('25', '32', 1)
        if '355' in str:
            str = str.replace('355', '25', 1)
        if '555' in str:
            str = str.replace('555', '3', 1)
    s = 0
    for i in range(len(str)):
        s += int(str[i])
    if s == 17:
        print(n)
        break