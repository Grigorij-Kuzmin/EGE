n = list(map(int, open('17_6605.txt').readlines()))
m = -10000
ma = 0
count = 0
for i in range(len(n)):
    if n[i] % 10 == 5:
        ma = max(ma, n[i])
for i in range(len(n) - 1):
    if (n[i] % 10 == 5 and n[i + 1] % 10 != 5) or (n[i] % 10 != 5 and n[i + 1] % 10 == 5):
        if abs(n[i] ** 2 - n[i + 1] ** 2) <= ma ** 2:
            count += 1
            m = max(m, abs(n[i] ** 2 - n[i + 1] ** 2))
print(count, m)