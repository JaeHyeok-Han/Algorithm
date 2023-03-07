import sys

n, m, block = list(map(int, sys.stdin.readline().strip().split(' ')))
game_map = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]

ans_t = sys.maxsize
ans_h = 0
for h in range(257):
    plus = 0
    minus = 0
    for i in range(n):
        for j in range(m):
            if game_map[i][j] > h:
                plus += (game_map[i][j] - h)
            else:
                minus += (h - game_map[i][j])
    if (plus + block) >= minus:
        if 2 * plus + minus <= ans_t:
            ans_t = 2 * plus + minus
            ans_h = h

print(ans_t, ans_h)
