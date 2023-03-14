import sys
from collections import deque

N, E = list(map(int, sys.stdin.readline().strip().split(' ')))
ground = [[0 for _ in range(N)] for _ in range(N)]
visited = [0 for _ in range(N)]
answer = 0

for _ in range(E):
    n1, n2 = list(map(int, sys.stdin.readline().strip().split(' ')))
    ground[n1 - 1][n2 - 1] = 1
    ground[n2 - 1][n1 - 1] = 1


def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        cur = queue.pop()
        for index in range(N):
            if ground[cur][index] and not visited[index]:
                visited[index] = 1
                queue.append(index)


for n in range(N):
    if visited[n]:
        continue
    else:
        answer += 1
        visited[n] = 1
        bfs(n)

print(answer)