from sys import stdin
from itertools import combinations
num, target = list(map(int, stdin.readline().strip().split(' ')))
numbers = list(map(int, stdin.readline().strip().split(' ')))
combi = list(filter(lambda x: x[0] + x[1] + x[2] <= target, list(combinations(numbers, 3))))
combi.sort(key=lambda x: -(x[0] + x[1] + x[2]))
print(sum(combi[0]))
