import sys
from itertools import combinations

N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
combi = list(combinations([str(i + 1) for i in range(N)], M))
for com in combi:
    print(' '.join(com))
