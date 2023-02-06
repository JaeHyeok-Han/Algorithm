import sys
h, m = list(map(int, sys.stdin.readline().strip().split(' ')))
total = h * 60 + m
total -= 45
total = total + 24 * 60 if total < 0 else total
print(f'{total // 60} {total % 60}')
