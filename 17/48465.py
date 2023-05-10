m = 10001
m1 = 0
count = 0
a = list(map(int, open('17.48465.txt').readlines()))
for i in range(len(a)):
    if abs(a[i]) % 10 == 6:
        m = min(m, a[i])
for i in range(len(a) - 1):
    if ((abs(a[i]) % 10 == 6 and abs(a[i + 1]) % 10 != 6) or (abs(a[i + 1]) % 10 == 6 and abs(a[i]) % 10 != 6)) and ((a[i] ** 2 + a[i + 1] ** 2) < m ** 2):
        count += 1
        m1 = max(m1, a[i] ** 2 + a[i + 1] ** 2)
print(count, m1)