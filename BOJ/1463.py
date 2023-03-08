import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
visited = {}
queue.append((n, 0))
visited[n] = 1

while queue:
    cur, count = queue.popleft()
    if cur == 1:
        print(count)
        break
    if cur % 3 == 0 and cur / 3 not in visited:
        queue.append((cur / 3, count + 1))
        visited[cur / 3] = 1
    if cur % 2 == 0 and cur / 2 not in visited:
        queue.append((cur / 2, count + 1))
        visited[cur / 2] = 1
    if cur - 1 not in visited:
        queue.append((cur - 1, count + 1))
        visited[cur - 1] = 1
