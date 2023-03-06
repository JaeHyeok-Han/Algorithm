import sys
from itertools import combinations

c, r = list(map(int, sys.stdin.readline().strip().split(' ')))
print(len(list(combinations(range(c), r))))
