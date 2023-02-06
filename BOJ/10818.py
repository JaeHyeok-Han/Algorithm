import sys
count = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().strip().split(' ')))
print(f'{min(numbers)} {max(numbers)}')
