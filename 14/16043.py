x = 9**7 + 3**21 - 9
count = 0
while x > 0:
    if x % 3 == 2:
        count += 1
    x //= 3
print(count)