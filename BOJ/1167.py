import sys
from collections import deque
from heapq import heappop, heappush

N = int(sys.stdin.readline())
edge = [[] for _ in range(N + 1)]
for _ in range(N):
    s, *info, _ = list(map(int, sys.stdin.readline().strip().split(' ')))
    for i in range(0, len(info), 2):
        edge[s].append([info[i + 1], info[i]])


def bfs(start):
    visited = [-1 for _ in range(N + 1)]
    visited[start] = 0
    h = []
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        for d, e in edge[cur]:
            if visited[e] == -1:
                q.append(e)
                visited[e] = visited[cur] + d
                heappush(h, (-visited[e], e))
    return heappop(h)


print(-bfs(bfs(1)[1])[0])
