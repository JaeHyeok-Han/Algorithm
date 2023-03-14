import sys
from collections import deque

N = int(sys.stdin.readline())
E = int(sys.stdin.readline())
ground = [[0 for _ in range(N)] for _ in range(N)]
visited = [0 for _ in range(N)]
answer = 0

for _ in range(E):
    n1, n2 = list(map(int, sys.stdin.readline().strip().split(' ')))
    ground[n1 - 1][n2 - 1] = 1
    ground[n2 - 1][n1 - 1] = 1

queue = deque()
queue.append(0)
visited[0] = 1
while queue:
    cur = queue.pop()
    for index in range(N):
        if ground[cur][index] and not visited[index]:
            answer += 1
            visited[index] = 1
            queue.append(index)
print(answer)
