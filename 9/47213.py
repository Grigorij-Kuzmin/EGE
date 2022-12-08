c = 0
with open('9.txt') as f:
    for line in f:
        nums = list(map(int, line.split('\t')))
        if len(nums) - len(set(nums)) == 1:
            s = sum(nums) - sum(set(nums))
            if (sum(set(nums)) - s) / 4 <= 2 * s:
                c += 1
print(c)




