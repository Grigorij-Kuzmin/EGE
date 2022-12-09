nums = list(map(int, open('47221.txt').readlines()))
count = 0
m = -10001
for i in range(len(nums)):
    if int(abs(nums[i])) % 10 == 3:
        m = max(m, int(nums[i]))
maxSum = -10001
for i in range(len(nums) - 1):
    if (nums[i] ** 2 + nums[i + 1] ** 2 >= m ** 2) and ((abs(nums[i]) % 10 == 3 and abs(nums[i + 1]) % 10 != 3) or (abs(nums[i]) % 10 != 3 and abs(nums[i + 1]) % 10 == 3)):
        count += 1
        maxSum = max(maxSum, nums[i] ** 2 + nums[i + 1] ** 2)
print(count, maxSum)