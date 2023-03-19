import sys

n, m = list(map(int, sys.stdin.readline().strip().split(' ')))
if m > (n // 2):
    m = n - m

ja = 1
for i in [i for i in range(n, n - m, -1)]:
    ja *= i
mo = 1
for i in [i for i in range(1, m + 1)]:
    mo *= i

print(ja // mo)
