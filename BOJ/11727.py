import sys

N = int(sys.stdin.readline())
dp = [1, 1, 3]
for i in range(3, 1001):
    dp.append(dp[i - 2] * 2 + dp[i - 1])
print(dp[N] % 10007)
