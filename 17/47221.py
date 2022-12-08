nums = list(map(int, open('17 (47221).txt').readlines()))
count = 0
m = max(nums)
MaxSum = -10001
for i in range(len(nums) - 1):
    if (nums[i] ** 2 + nums[i + 1] ** 2 >= m ** 2) and ((nums[i] % 10 == 3 and nums[i + 1] % 10 != 3) or (nums[i] % 10 != 3 and nums[i + 1] % 10 == 3)):
        count += 1
        maxSum = max(maxSum, nums[i] ** 2 + nums[i + 1] ** 2)
print(count, maxSum)