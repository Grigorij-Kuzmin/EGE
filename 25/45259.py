x = 0
for j in range(10):
    for i in range(10):
        x = int(f'12345{j}7{i}8')
        if x % 23 == 0:
            print(f'{x}     {x // 23}')