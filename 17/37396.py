count = 0
m = 0
a = list(map(int, open('17 (37396).txt').readlines()))
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if (abs(a[i] - a[j])) % 80 == 0:
            count += 1
            m = max(m, abs(a[i] - a[j]))
print(count, m)
