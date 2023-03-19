import sys
from collections import deque

good_case, bad_case = list(map(int, sys.stdin.readline().strip().split(' ')))
hidden = {}
for _ in range(good_case + bad_case):
    start, end = list(map(int, sys.stdin.readline().strip().split(' ')))
    hidden[start] = end

visited = [0] * 101
queue = deque()
queue.append((1, 0))
visited[1] = 1
while queue:
    cur, count = queue.popleft()
    if cur == 100:
        print(count)
        break
    for new in [cur + i for i in range(1, 7) if cur + i <= 100 and not visited[cur + i]]:
        if new in hidden:
            queue.append((hidden[new], count + 1))
            visited[hidden[new]] = 1
        else:
            queue.append((new, count + 1))
            visited[new] = 1
