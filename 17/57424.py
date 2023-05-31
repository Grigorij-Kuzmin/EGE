count = 0
x = 0
m = 0
a = list(map(int, open('1_17.txt').readlines()))
for i in range(len(a)):
    if 9 < a[i] < 100:
        x = max(x, a[i])
for i in range(len(a) - 1):
    if (((9 < a[i] < 100) and (a[i + 1] > 100 or a[i + 1] < 10)) or ((9 < a[i + 1] < 100) and (a[i] > 100 or a[i] < 10))) and ((a[i] + a[i + 1]) % x == 0):
        count += 1
        m = max(m, a[i] + a[i + 1])
print(count, m)