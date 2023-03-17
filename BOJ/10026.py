import sys
from collections import deque

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = int(sys.stdin.readline())
ground = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
normal_ans = 0
special_ans = 0
queue = deque()
color = ''

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            normal_ans += 1
            color = ground[i][j]
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                cur_x, cur_y = queue.popleft()
                for k in range(4):
                    new_x = cur_x + direction[k][0]
                    new_y = cur_y + direction[k][1]
                    if 0 <= new_x < N and 0 <= new_y < N and not visited[new_x][new_y] and ground[new_x][new_y] == color:
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = 1

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            special_ans += 1
            color = ground[i][j]
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                cur_x, cur_y = queue.popleft()
                for k in range(4):
                    new_x = cur_x + direction[k][0]
                    new_y = cur_y + direction[k][1]
                    if 0 <= new_x < N and 0 <= new_y < N and not visited[new_x][new_y]:
                        if color == 'B':
                            if ground[new_x][new_y] == 'B':
                                queue.append((new_x, new_y))
                                visited[new_x][new_y] = 1
                        else:
                            if ground[new_x][new_y] == 'R' or ground[new_x][new_y] == 'G':
                                queue.append((new_x, new_y))
                                visited[new_x][new_y] = 1

print(f'{normal_ans} {special_ans}')
