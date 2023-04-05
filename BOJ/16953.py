import sys
from collections import deque

init, target = list(map(int, sys.stdin.readline().strip().split(' ')))
visited = {
    init: 1
}
queue = deque()
queue.append(init)
while queue:
    cur = queue.popleft()
    for n in [cur * 2, int(str(cur) + '1')]:
        if n not in visited and n <= target:
            queue.append(n)
            visited[n] = visited[cur] + 1

if target in visited:
    print(visited[target])
else:
    print(-1)
