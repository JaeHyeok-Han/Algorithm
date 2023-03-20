import sys
from itertools import combinations_with_replacement

N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
combi = list(combinations_with_replacement([str(i + 1) for i in range(N)], M))
for com in combi:
    print(' '.join(com))
