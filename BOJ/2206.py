import sys
from collections import deque

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
ground = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
dp = [[[-1] * M for _ in range(N)] for _ in range(2)]
dp[0][0][0] = 1
queue = deque([(0, 0, 0)])

while queue:
    is_break, cur_x, cur_y = queue.popleft()
    for d_x, d_y in delta:
        next_x = cur_x + d_x
        next_y = cur_y + d_y
        if 0 <= next_x < N and 0 <= next_y < M:
            if is_break == 0:
                if ground[next_x][next_y] == 0 and dp[0][next_x][next_y] == -1:
                    dp[0][next_x][next_y] = dp[0][cur_x][cur_y] + 1
                    queue.append((0, next_x, next_y))
                elif ground[next_x][next_y] == 1 and dp[1][next_x][next_y] == -1:
                    dp[1][next_x][next_y] = dp[0][cur_x][cur_y] + 1
                    queue.append((1, next_x, next_y))
            elif is_break == 1:
                if ground[next_x][next_y] == 0 and dp[1][next_x][next_y] == -1:
                    dp[1][next_x][next_y] = dp[1][cur_x][cur_y] + 1
                    queue.append((1, next_x, next_y))

if dp[0][N - 1][M - 1] == -1 and dp[1][N - 1][M - 1] == -1:
    print(-1)
elif dp[0][N - 1][M - 1] == -1:
    print(dp[1][N - 1][M - 1])
elif dp[1][N - 1][M - 1] == -1:
    print(dp[0][N - 1][M - 1])
else:
    print(min(dp[0][N - 1][M - 1], dp[1][N - 1][M - 1]))
