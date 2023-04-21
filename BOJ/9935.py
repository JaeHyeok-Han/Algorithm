import sys

string = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()
stack = []
for char in string:
    stack.append(char)
    if len(stack) >= len(target):
        if ''.join(stack[len(stack) - len(target):]) == target:
            for _ in range(len(target)):
                stack.pop()

answer = ''.join(stack)
print(answer if answer else 'FRULA')
