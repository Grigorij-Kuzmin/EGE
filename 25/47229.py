x = 0
i = 0
while x <= 10 ** 10:
    for j in range(10):
        if j != 0:
            x = int(f'1{j}2139{i}4')
        else:
            x = int(f'1{j}21394')
        if x % 2023 == 0:
            print(f'{x}     {x // 2023}')
    i += 1