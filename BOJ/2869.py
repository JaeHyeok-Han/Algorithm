import sys
from math import ceil

a, b, v = list(map(int, sys.stdin.readline().strip().split(' ')))
answer = 0

answer += ceil((v - a) / (a - b))
answer += 1
print(answer)
