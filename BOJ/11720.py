import sys
count = sys.stdin.readline()
numbers = sys.stdin.readline().strip()
answer = 0
for number in numbers:
    answer += int(number)
print(answer)
