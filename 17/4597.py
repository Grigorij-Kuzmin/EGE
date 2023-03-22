nums = list(map(int, open('4597.txt').readlines()))
count = 0
maxSum = 0
m = min(nums)
for i in range(len(nums) - 1):
    if nums[i] % 117 == m or nums[i + 1] % 117 == m:
        count += 1
        maxSum = max(maxSum, nums[i] + nums[i + 1])
print(count, maxSum)