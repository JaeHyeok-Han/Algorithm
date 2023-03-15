import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = int(sys.stdin.readline())
ground = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    ans_obj[answer] += 1
    while queue:
        cur_x, cur_y = queue.popleft()
        for idx in range(4):
            new_x = cur_x + dx[idx]
            new_y = cur_y + dy[idx]
            if 0 <= new_x < N and 0 <= new_y < N and ground[new_x][new_y] and not visited[new_x][new_y]:
                ans_obj[answer] += 1
                visited[new_x][new_y] = 1
                queue.append((new_x, new_y))


answer = 0
ans_obj = {}
for i in range(N):
    for j in range(N):
        if ground[i][j] and not visited[i][j]:
            answer += 1
            ans_obj[answer] = 0
            bfs(i, j)
ans_arr = [ans_obj[i] for i in ans_obj]
ans_arr.sort()
print(answer)
for i in ans_arr:
    print(i)
