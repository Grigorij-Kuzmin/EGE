for x in range(16):
    s = int(f'97968{x}13', 15) + int(f'7{x}213', 15)
    if s % 14 == 0:
        print(s / 14)