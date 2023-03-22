str = ''
while str != 70 * '1' + 56 * '2' + 23 * '3':
    for x in range(100):
        for y in range(100):
            for z in range(100):
                str = '0' + x * '1' + y * '2' + z * '3' + '0'
                while '00' not in str:
                    str = str.replace('01', '210', 1)
                    str = str.replace('02', '3101', 1)
                    str = str.replace('03', '2012', 1)
print(x + y + z + 2)