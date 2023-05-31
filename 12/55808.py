for n in range(3, 100):
    s = 0
    str = '3' + n * '5'
    while '25' in str or '355' in str or '555' in str:
        if '25' in str:
            str = str.replace('25', '3', 1)
        if '355' in str:
            str = str.replace('355', '52', 1)
        if '555' in str:
            str = str.replace('555', '23', 1)
    for i in range(len(str)):
        s += int(str[i])
    if s == 27:
        print(n)