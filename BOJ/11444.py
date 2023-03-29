import sys

MOD = 1000000007
N = int(sys.stdin.readline())
dp = {
    0: 0,
    1: 1
}


def get_fibo(n):
    if n in dp:
        return dp[n]
    else:
        if n % 2:
            dp[n] = (get_fibo(((n - 1) // 2) + 1) ** 2 + get_fibo((n - 1) // 2) ** 2) % MOD
        else:
            dp[n] = (get_fibo(n // 2) * (get_fibo(n // 2) + 2 * get_fibo((n // 2) - 1))) % MOD
        return dp[n]


if N < 2:
    print(dp[N])
else:
    print(get_fibo(N))
