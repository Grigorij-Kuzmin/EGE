nums = list(map(int, open('17.txt').readlines()))
count = 0
maxSum = -20001
for i in range(len(nums) - 1):
    if nums[i] % 3 == 0 or nums[i + 1] % 3 == 0:
        count += 1
        maxSum = max(maxSum, nums[i] + nums[i + 1])
print(count, maxSum)
