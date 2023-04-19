def f(x, step, nums):
    if x == 13:
        nums.add(x)
    else:
        f(x - 3, step, nums)
        f(x * (-3), step + 1, nums)


s = set
f(333, 0, s)
print(len(([n for n in s if n < 0])))


