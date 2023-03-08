import sys

n, r, c = list(map(int, sys.stdin.readline().strip().split(' ')))
answer = 0

while n > 1:
    if r < 2 ** (n - 1) and c < 2 ** (n - 1):
        n -= 1
    elif r < 2 ** (n - 1) and c < 2 ** n:
        answer += (2 ** (n - 1)) ** 2
        c -= 2 ** (n - 1)
        n -= 1
    elif r < 2 ** n and c < 2 ** (n - 1):
        answer += ((2 ** (n - 1)) ** 2) * 2
        r -= 2 ** (n - 1)
        n -= 1
    else:
        answer += ((2 ** (n - 1)) ** 2) * 3
        r -= 2 ** (n - 1)
        c -= 2 ** (n - 1)
        n -= 1

if r == 0 and c == 0:
    answer += 0
elif r == 0 and c == 1:
    answer += 1
elif r == 1 and c == 0:
    answer += 2
else:
    answer += 3

print(answer)
