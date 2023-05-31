m = 100001
count = 0
minsum = 200002
a = list(map(int, open('17 (55813).txt').readlines()))
for i in range(len(a)):
    if a[i] % 10 == 5:
        m = min(m, a[i])
for i in range(len(a) - 1):
    if ((100 <= a[i] < 1000) and (a[i + 1] < 100 or a[i + 1] >= 1000) or (100 <= a[i + 1] < 1000) and (a[i] < 100 or a[i] >= 1000)) and ((a[i] + a[i + 1]) % m == 0):
        minsum = min(minsum, a[i] + a[i + 1])
        count += 1
print(count, minsum)