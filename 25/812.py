def simple(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True


for i in range(33333, 55556):
    x = i
    a = []
    while x != 0:
        a.append(x % 10)
        x = x // 10
    if 35 < sum(a) and simple(i):
        print(i)
