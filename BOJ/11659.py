import sys

N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
nums = list(map(int, sys.stdin.readline().strip().split(' ')))
new_nums = [0]
for i in range(N):
    new_nums.append(new_nums[i] + nums[i])
for _ in range(M):
    start, end = list(map(int, sys.stdin.readline().strip().split(' ')))
    if start == end:
        print(nums[end - 1])
    else:
        print(new_nums[end] - new_nums[start - 1])
