def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for x, y in puddles:
        dp[y - 1][x - 1] = -1

    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            temp = 0
            if 0 <= (i - 1) and dp[i - 1][j] != -1:
                temp += dp[i - 1][j]
            if 0 <= (j - 1) and dp[i][j - 1] != -1:
                temp += dp[i][j - 1]
            dp[i][j] += temp % 1000000007
    return dp[n - 1][m - 1]
