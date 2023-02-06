import sys
numbers = list(map(int, sys.stdin.readline().strip().split(' ')))
answer = 0
for number in numbers:
    answer += number ** 2
print(answer % 10)
