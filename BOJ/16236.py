import sys

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
answer = 0

N = int(sys.stdin.readline())
ground = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]

level = 2
eat = 0
queue = []
visited = [[-1] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if ground[i][j] == 9:
            queue.append((i, j))
            ground[i][j] = 0
            visited[i][j] = 0

while queue:
    fish = []
    for cur in queue:
        cur_x, cur_y = cur
        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N and ground[new_x][new_y] <= level and visited[new_x][new_y] == -1:
                fish.append((new_x, new_y))
                visited[new_x][new_y] = visited[cur_x][cur_y] + 1
    queue.clear()
    can = []
    for f in fish:
        cur_x, cur_y = f
        if 0 < ground[cur_x][cur_y] < level:
            can.append((cur_x, cur_y))
        else:
            queue.append((cur_x, cur_y))
    if can:
        can.sort(key=lambda x: (x[0], x[1]))
        cur_x, cur_y = can[0]
        eat += 1
        if eat == level:
            level += 1
            eat = 0
        answer += visited[cur_x][cur_y]
        visited = [[-1] * N for _ in range(N)]
        queue.clear()
        queue.append((cur_x, cur_y))
        ground[cur_x][cur_y] = 0
        visited[cur_x][cur_y] = 0

print(answer)
