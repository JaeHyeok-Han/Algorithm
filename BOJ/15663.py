import sys
from itertools import permutations

N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
nums = list(map(int, sys.stdin.readline().strip().split(' ')))
combi = list(set(permutations(nums, M)))
combi.sort()
for com in combi:
    print(' '.join(list(map(str, com))))
