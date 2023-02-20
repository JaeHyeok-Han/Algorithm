import sys
num1, num2 = list(map(int, sys.stdin.readline().strip().split(' ')))


def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


ans1 = gcd(num1, num2)
ans2 = num1 * num2 / ans1
print(ans1)
print(int(ans2))
