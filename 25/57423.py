x = 0
j = - 1
while x <= 10 ** 8:
    for i in range(10):
        for o in range(10):
            if j == -1:
                x = int(f'12{i}{o}156')
            else:
                x = int(f'12{i}{o}1{j}56')
            if x % 317 == 0:
                print(f'{x}     {x // 317}')
    j += 1