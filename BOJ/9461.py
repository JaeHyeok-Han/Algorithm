import sys

nums = [1, 1, 1]
for i in range(3, 101):
    nums.append(nums[i - 2] + nums[i - 3])
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    print(nums[int(sys.stdin.readline()) - 1])
