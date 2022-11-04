for x in range(0, 9):
    for y in range(0, 9):
        num = int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)
        if num % 61 == 0:
            print(num // 61)