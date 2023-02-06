import sys
number_count, target = list(map(int, sys.stdin.readline().strip().split(' ')))
numbers = list(map(int, sys.stdin.readline().strip().split(' ')))
answer = ''
for number in numbers:
    if number < target:
        answer += f'{number} '
print(answer.strip())
