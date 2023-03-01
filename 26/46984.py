m = [[0 for i in range(10001)]for j in range(10001)]
with open('46984.txt') as f:
    lines = f.readlines()[1:]
    for line in lines:
        x, y = list(map(int, line.split()))
        m[x][y] = 1
print(m)