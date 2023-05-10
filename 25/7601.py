j = -1
x = 0
while x <= 10 ** 8:
    for i in range(10):
        for o in range(10):
            if j == -1:
                x = int(f'12{i}{o}361')
            else:
                x = int(f'12{i}{o}36{j}1')
            if x % 273 == 0:
                print(f'{x}     {x//273}')
    j += 1