with open('47230.txt') as f:
    a = [int(f.readline())]
    a.sort()
    l = 0
    m = 0
    for i in range(len(a)):
        if a[i] + 3 <= a[i + 1]:
            l += 1
            m = max(l, m)
