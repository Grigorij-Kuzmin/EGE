i = 0
m = 0
while m <= 10 ** 8:
    m = int(f'123{i}890')
    i += 1
    if m % 27 == 0:
        print(f'{m}         {m // 27}')