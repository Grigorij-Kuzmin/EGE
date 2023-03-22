for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            str = '0' + x * '1' + y * '2' + z * '3' + '0'
            while '00' not in str:
                str = str.replace('01', '210', 1)
                str = str.replace('02', '320', 1)
                str = str.replace('03', '3012', 1)
            if str.count('1') == 26 and str.count('2') == 54 and str.count('3') == 48:
                print(x + y + z + 2)