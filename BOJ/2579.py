import sys

N = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(N)]
if N < 3:
    print(sum(score))
else:
    dp = [[-1] * N for _ in range(2)]
    dp[0][0] = score[0]
    dp[1][0] = 0
    dp[0][1] = score[0] + score[1]
    dp[1][1] = score[1]
    for i in range(2, N):
        dp[0][i] = dp[1][i - 1] + score[i]
        dp[1][i] = max(dp[0][i - 2], dp[1][i - 2]) + score[i]
    print(max(dp[0][N - 1], dp[1][N - 1]))
