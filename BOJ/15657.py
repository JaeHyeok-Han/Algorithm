import sys
from itertools import combinations_with_replacement

N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
nums = sys.stdin.readline().strip().split(' ')
nums.sort(key=lambda x: (int(x)))
combi = list(combinations_with_replacement(nums, M))
for com in combi:
    print(' '.join(com))
    