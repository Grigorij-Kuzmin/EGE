import itertools
for x in range(2, 100):
    strings = itertools.product('12', repeat=x)
    for str in strings:
        str = '0' + ''.join(str) + '0'
        if str.count('1') == str.count('2'):
            while '00' not in str:
                if '011' in str:
                    str = str.replace('011', '101', 1)
                else:
                    str = str.replace('01', '40', 1)
                    str = str.replace('02', '20', 1)
                    str = str.replace('0222', '1401', 1)
            if str.count('1') == 6 and str.count('2') == 9:
                print(str.count('4'))