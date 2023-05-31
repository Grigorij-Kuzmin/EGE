a = []
m = 100001
count = 0
min1 = 999999
with open('17_7596.txt') as f:
    for line in f:
        a.append(int(line))
    for i in range(len(a)):
        if (99 < a[i] < 1000) and (a[i] % 10 == 5):
            m = min(m, a[i])
    for j in range(len(a) - 1):
        x = (a[j] + a[j + 1])
        f1 = 1000 > a[j] > 99
        f2 = 1000 > a[j + 1] > 99
        if ((f1 and (not f2)) or (f2 and (not f1))) and (x % m == 0):
            count += 1
            min1 = min(min1, x)
print(count, min1)