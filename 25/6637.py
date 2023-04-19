'''m = 0
j = 0
while m <= 10 ** 10:
    for i in range(10):
        if j != 0:
            m = int(f'1{i}2139{j}4')
        else:
            m = int(f'1{i}21394')
        if m % 3052 == 0:
            print(f'{m}     {m / 3052}')
    j += 1'''
from fnmatch import fnmatch

for i in range(0, 10 ** 10 + 1, 3052):
    if i % 3052 == 0 and fnmatch(str(i), '1?2139*4'):
        print(f'{i}     {i // 3052}')
