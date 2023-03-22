max = 0
count = 0
g = 0
m = [[0 for i in range(10001)]for j in range(10001)]
with open('46984.txt') as f:
    lines = f.readlines()[1:]
    for line in lines:
        x, y = list(map(int, line.split()))
        m[x][y] = 1
    for x in range(len(m)):
        for y in range(len(m[x]) - 1):
            if m[x][y] == 1:
                count += 1
                if max < count:
                    max = count
                    g = x
            else:
                count = 0
print(g, max)