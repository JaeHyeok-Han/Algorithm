import sys

N = int(sys.stdin.readline())
ground = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
ans = [0, 0]


def solution(sub_ground):
    n = len(sub_ground)
    if n == 1:
        if sub_ground[0][0]:
            ans[1] += 1
            return
        else:
            ans[0] += 1
            return

    temp_one = 0
    for i in range(n):
        for j in range(n):
            if sub_ground[i][j]:
                temp_one += 1

    if temp_one == n ** 2:
        ans[1] += 1
        return
    elif temp_one == 0:
        ans[0] += 1
        return
    else:
        new_n = n // 2
        sub = []
        sub_row = sub_ground[0:new_n]
        for row in sub_row:
            sub.append(row[0:new_n])
        solution(sub)
        sub = []
        sub_row = sub_ground[0:new_n]
        for row in sub_row:
            sub.append(row[new_n:n])
        solution(sub)
        sub = []
        sub_row = sub_ground[new_n:n]
        for row in sub_row:
            sub.append(row[0:new_n])
        solution(sub)
        sub = []
        sub_row = sub_ground[new_n:n]
        for row in sub_row:
            sub.append(row[new_n:n])
        solution(sub)


solution(ground)
for i in ans:
    print(i)
