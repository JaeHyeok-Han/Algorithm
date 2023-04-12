def solution(land):
    n = len(land)
    dp = [[-1] * 4 for _ in range(n)]
    for i in range(4):
        dp[0][i] = land[0][i]
    for i in range(1, n):
        for j in range(4):
            dp[i][j] = land[i][j] + max([dp[i - 1][k] for k in range(4) if k != j])
    return max(dp[n - 1])
