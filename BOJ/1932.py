import sys

N = int(sys.stdin.readline())
ground = []
dp = [[0] * (i + 1) for i in range(N)]
for _ in range(N):
    ground.append(list(map(int, sys.stdin.readline().strip().split(' '))))

dp[0][0] = ground[0][0]
for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + ground[i][0]
    dp[i][i] = dp[i - 1][i - 1] + ground[i][i]
for i in range(2, N):
    for j in range(1, i):
        dp[i][j] = ground[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[N - 1]))
