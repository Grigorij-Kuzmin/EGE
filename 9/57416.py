count = 0
with open('1_9.txt') as f:
    for line in f:
        s = list(map(int, line.strip().split('\t')))
        x = max(s) + min(s)
        y = sum(s) - x
        if (len(s) == len(set(s))) and (2 * x <= y):
            count += 1
print(count)


