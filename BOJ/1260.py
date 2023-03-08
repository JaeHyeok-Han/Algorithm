import sys
from collections import deque

sys.setrecursionlimit(10 ** 5)

n, e, start = list(map(int, sys.stdin.readline().strip().split(' ')))
edge = [[] for _ in range(n)]
for _ in range(e):
    n1, n2 = list(map(int, sys.stdin.readline().strip().split(' ')))
    edge[n1 - 1].append(n2 - 1)
    edge[n2 - 1].append(n1 - 1)
for i in range(n):
    edge[i].sort()


def dfs(s):
    visited[s] = 1
    print(s + 1, end=' ')
    for ele in edge[s]:
        if not visited[ele]:
            dfs(ele)


def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        cur = queue.popleft()
        print(cur + 1, end=' ')
        for ele in edge[cur]:
            if not visited[ele]:
                visited[ele] = 1
                queue.append(ele)


visited = [0 for _ in range(n)]
dfs(start - 1)
print()
visited = [0 for _ in range(n)]
bfs(start - 1)
