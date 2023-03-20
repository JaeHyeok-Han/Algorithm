import sys
from collections import deque

direction = [(-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0)]
M, N, H = list(map(int, sys.stdin.readline().strip().split(' ')))
ground = [[list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)] for _ in range(H)]
visited = [[[-1] * M for _ in range(N)] for _ in range(H)]
zero = 0
answer = 0
queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if ground[i][j][k] == 1:
                queue.append((i, j, k))
                visited[i][j][k] = 0
            elif not ground[i][j][k]:
                zero += 1

while queue:
    cur_i, cur_j, cur_k = queue.popleft()
    for d in direction:
        new_i = cur_i + d[0]
        new_j = cur_j + d[1]
        new_k = cur_k + d[2]
        if 0 <= new_i < H and 0 <= new_j < N and 0 <= new_k < M and not ground[new_i][new_j][new_k] and visited[new_i][new_j][new_k] == -1:
            zero -= 1
            queue.append((new_i, new_j, new_k))
            visited[new_i][new_j][new_k] = visited[cur_i][cur_j][cur_k] + 1
            answer = answer if answer >= visited[cur_i][cur_j][cur_k] + 1 else visited[cur_i][cur_j][cur_k] + 1

if zero:
    print(-1)
else:
    print(answer)
