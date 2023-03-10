import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split(' ')))
answer = {}
set_nums = sorted(set(nums))
for i, num in enumerate(set_nums):
    answer[num] = i
for num in nums:
    print(answer[num], end=' ')
