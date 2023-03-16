count = 0
with open('09.6602.txt') as f:
    for line in f:
        nums = list(map(int, line.split('\t')))
        if len(nums) - len(set(nums)) == 1:
            s = 2 * (sum(nums) - sum(set(nums)))
            if ((sum(set(nums)) - s / 2) / 4) >= s:
                count += 1
print(count)