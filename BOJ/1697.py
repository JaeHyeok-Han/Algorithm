import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().strip().split(' ')))
queue = deque()
queue.append(N)
visited = {
    N: 0
}

while queue:
    cur = queue.popleft()
    if cur == K:
        print(visited[cur])
        break
    new_cur = [cur - 1, cur + 1, cur * 2]
    for new in new_cur:
        if 0 <= new <= 100000 and new not in visited:
            queue.append(new)
            visited[new] = visited[cur] + 1
