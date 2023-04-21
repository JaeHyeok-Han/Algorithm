import sys
from collections import deque

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
ground = [list(map(int, list(sys.stdin.readline().strip().split(' ')))) for _ in range(N)]
answer = 0


def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[0] * M for _ in range(N)]
    temp = [[0] * M for _ in range(N)]
    will_del = set()
    visited[x][y] = 1
    while queue:
        cur_x, cur_y = queue.popleft()
        for dx, dy in delta:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
                if ground[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    queue.append((next_x, next_y))
                elif ground[next_x][next_y] == 1:
                    temp[next_x][next_y] += 1
                    if temp[next_x][next_y] >= 2:
                        will_del.add((next_x, next_y))
    return will_del


while True:
    del_list = bfs(0, 0)
    if len(del_list) == 0:
        break
    else:
        answer += 1
        for del_x, del_y in del_list:
            ground[del_x][del_y] = 0

print(answer)
