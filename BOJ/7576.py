import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
M, N = list(map(int, sys.stdin.readline().strip().split(' ')))
box = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
arr = []

temp = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            arr.append((i, j))
            box[i][j] = 1
        elif box[i][j] == -1:
            pass
        else:
            temp += 1

answer = 1
if not temp:
    print(0)
else:
    while arr:
        answer += 1
        cur_arr = arr[:]
        arr = []
        for cur in cur_arr:
            cur_x, cur_y = cur
            for i in range(4):
                new_x = cur_x + dx[i]
                new_y = cur_y + dy[i]
                if 0 <= new_x < N and 0 <= new_y < M and not box[new_x][new_y]:
                    arr.append((new_x, new_y))
                    box[new_x][new_y] = 1
                    temp -= 1

    if temp:
        print(-1)
    else:
        print(answer - 2)
