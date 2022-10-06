def f(str):
    while '00' not in str:
        str = str.replace('01', '210')
        str = str.replace('02', '3101')
        str = str.replace('03', '2012')
    return str

for i1 in range(1, 100):
    for i2 in range(1, 100):
        for i3 in range(1, 100):
            s = '0' + '1' * i1 + '2' * i2 + '3' * i3 + '0';
            res = f(s)
            if res.count('1') == 61 and res.count('2') == 50 and res.count('3') == 18:
                print(s)