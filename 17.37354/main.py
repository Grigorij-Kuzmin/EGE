nums = list(map(int, open('17.txt').readlines()))
count = 0
maxSum = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j]) % 2 != 0 and (nums[i] * nums[j]) % 5 == 0:
            count += 1
            maxSum = max(maxSum, nums[i] + nums[j])
print(count, maxSum)