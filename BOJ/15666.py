import sys
from itertools import combinations_with_replacement

N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
nums = list(map(int, sys.stdin.readline().strip().split(' ')))
nums.sort()
combi = list(set(combinations_with_replacement(nums, M)))
combi.sort()
for com in combi:
    print(' '.join(list(map(str, com))))
