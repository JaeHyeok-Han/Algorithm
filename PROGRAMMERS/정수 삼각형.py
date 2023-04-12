def solution(triangle):
    n = len(triangle)
    dp = [[0] * (i + 1) for i in range(n)]
    for i in range(n):
        dp[i][0] = dp[i - 1][0] + triangle[i][0]
        dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
    if n > 2:
        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = triangle[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])
    return max(dp[n - 1])
