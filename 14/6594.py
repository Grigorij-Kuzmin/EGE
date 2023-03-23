for x in range(13):
    y = int(f'753{x}2', 13) + int(f'2{x}173', 13)
    if y % 12 == 0:
        print(y // 12)
        break