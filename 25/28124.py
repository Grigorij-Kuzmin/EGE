m = 0
s = 6000000
for i in range(568023, 569230):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
            if m <= count:
                m = count
                s = i
print(m, s)