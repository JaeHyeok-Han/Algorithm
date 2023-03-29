import sys
from collections import deque
from heapq import heappop, heappush

N = int(sys.stdin.readline())
edge = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e, w = list(map(int, sys.stdin.readline().strip().split(' ')))
    edge[s].append([w, e])
    edge[e].append([w, s])


def bfs(start):
    visited = [-1 for _ in range(N + 1)]
    visited[start] = 0
    h = []
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        for dist, end in edge[cur]:
            if visited[end] == -1:
                q.append(end)
                visited[end] = visited[cur] + dist
                heappush(h, (-visited[end], end))
    return heappop(h)


if N == 1:
    print(0)
else:
    print(-bfs(bfs(1)[1])[0])
