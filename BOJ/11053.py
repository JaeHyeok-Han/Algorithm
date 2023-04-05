import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split(' ')))
dp = [-1] * N
dp[0] = 1

for i in range(1, N):
    max_dp = 0
    for j in range(i):
        if nums[j] < nums[i]:
            if dp[j] > max_dp:
                max_dp = dp[j]
    dp[i] = max_dp + 1

print(max(dp))
