for x in range(16):
    y = int(f'8{x}84{x}', 16) + int(f'78{x}34', 16)
    if y % 23 == 0:
        print(y // 23)