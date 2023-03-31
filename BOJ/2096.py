import sys

N = int(sys.stdin.readline())
if N == 1:
    nums = list(map(int, sys.stdin.readline().strip().split(' ')))
    print(max(nums), min(nums))
else:
    max_nums = []
    min_nums = []
    for i in range(N):
        nums = list(map(int, sys.stdin.readline().strip().split(' ')))
        if i == 0:
            max_nums = nums[:]
            min_nums = nums[:]
        else:
            max_temp = max_nums[:]
            min_temp = min_nums[:]
            max_nums[0] = nums[0] + max(max_temp[0], max_temp[1])
            min_nums[0] = nums[0] + min(min_temp[0], min_temp[1])
            max_nums[1] = nums[1] + max(max_temp[0], max_temp[1], max_temp[2])
            min_nums[1] = nums[1] + min(min_temp[0], min_temp[1], min_temp[2])
            max_nums[2] = nums[2] + max(max_temp[1], max_temp[2])
            min_nums[2] = nums[2] + min(min_temp[1], min_temp[2])

    print(max(max_nums), min(min_nums))
