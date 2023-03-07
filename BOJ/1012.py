import sys
from collections import deque

test_case_count = int(sys.stdin.readline())
for _ in range(test_case_count):
    answer = 0
    m, n, count = list(map(int, sys.stdin.readline().strip().split(' ')))
    ground = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(count):
        i, j = list(map(int, sys.stdin.readline().strip().split(' ')))
        ground[j][i] = 1

    def bfs(_i, _j):
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        que = deque()
        que.append([_i, _j])
        while que:
            cur_i, cur_j = que.popleft()
            for k in range(4):
                new_i = cur_i + dx[k]
                new_j = cur_j + dy[k]
                if 0 <= new_i < n and 0 <= new_j < m and ground[new_i][new_j] and not visited[new_i][new_j]:
                    visited[new_i][new_j] = 1
                    que.append([new_i, new_j])

    for i in range(n):
        for j in range(m):
            if not ground[i][j]:
                visited[i][j] = 1
            else:
                if not visited[i][j]:
                    answer += 1
                    bfs(i, j)
    print(answer)
