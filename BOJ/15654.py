import sys
from itertools import permutations

N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
nums = sys.stdin.readline().strip().split(' ')
nums.sort(key=lambda x: (int(x)))
combi = list(permutations(nums, M))
for com in combi:
    print(' '.join(com))
