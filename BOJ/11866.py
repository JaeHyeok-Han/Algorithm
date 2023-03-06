import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().strip().split(' ')))
arr = deque()
answer = []
for i in range(N):
    arr.append(i + 1)

while arr:
    for _ in range(K - 1):
        arr.append(arr.popleft())
    answer.append(arr.popleft())

print("<", end='')
for i, num in enumerate(answer):
    print(num, end='')
    if i != len(answer) - 1:
        print(", ", end='')
print(">", end='')
