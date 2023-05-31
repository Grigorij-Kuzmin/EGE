count = 0
with open('09_7588.txt') as f:
    for line in f:
        n = list(map(int, line.strip().split('\t')))
        if (len(n) - len(set(n)) == 0) and (3 * (min(n) + max(n)) <= 2 * (sum(n) - min(n) - max(n))):
            count += 1
print(count)

