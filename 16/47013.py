def f(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return f(n - 1) + 1
    if n % 2 == 0 and n > 0:
        return f(n / 2)


count = 0
for n in range(1000000000):
    if f(n) == 3:
        count += 1
    print(n, count)