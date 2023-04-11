import sys
from collections import deque

init, target = list(map(int, sys.stdin.readline().strip().split(' ')))
queue = deque()
queue.append(init)
visited = {
    init: 0
}

while queue:
    cur = queue.popleft()
    if cur == target:
        print(visited[cur])
        break
    for i, num in enumerate([cur * 2, cur - 1, cur + 1]):
        if 0 <= num <= 100000 and num not in visited:
            queue.append(num)
            if i == 0:
                visited[num] = visited[cur]
            else:
                visited[num] = visited[cur] + 1
