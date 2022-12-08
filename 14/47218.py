for x in range(15):
    n = int(f'123{x}5', 15) + int(f'1{x}233', 15)
    if n % 14 == 0:
        print(n // 14)

