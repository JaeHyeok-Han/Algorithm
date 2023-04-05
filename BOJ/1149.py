import sys

N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
dp = [[-1] * N for _ in range(3)]
dp[0][0] = costs[0][0]
dp[1][0] = costs[0][1]
dp[2][0] = costs[0][2]

for i in range(1, N):
    dp[0][i] = costs[i][0] + min(dp[1][i - 1], dp[2][i - 1])
    dp[1][i] = costs[i][1] + min(dp[0][i - 1], dp[2][i - 1])
    dp[2][i] = costs[i][2] + min(dp[0][i - 1], dp[1][i - 1])

print(min(dp[0][N - 1], dp[1][N - 1], dp[2][N - 1]))
