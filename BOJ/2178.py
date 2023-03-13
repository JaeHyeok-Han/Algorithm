import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
ground = []
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    ground.append(list(sys.stdin.readline().strip()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque()
queue.append((0, 0))
visited[0][0] = 1
while queue:
    curX, curY = queue.popleft()
    if curX == (N - 1) and curY == (M - 1):
        print(visited[curX][curY])
        break
    for i in range(4):
        newX = curX + dx[i]
        newY = curY + dy[i]
        if 0 <= newX < N and 0 <= newY < M and ground[newX][newY] == '1' and not visited[newX][newY]:
            visited[newX][newY] = visited[curX][curY] + 1
            queue.append((newX, newY))