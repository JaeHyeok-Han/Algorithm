import sys

N = int(sys.stdin.readline())
dp = [-1 for _ in range(1001)]
dp[1] = 1
dp[2] = 2


def t(n):
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = t(n - 1) + t(n - 2)
        return dp[n]


print(t(N) % 10007)
