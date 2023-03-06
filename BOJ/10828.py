import sys

command_count = int(sys.stdin.readline())
stack = []
for _ in range(command_count):
    input_str = sys.stdin.readline().strip().split(' ')
    command = input_str[0]
    if command == 'push':
        stack.append(int(input_str[1]))
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[len(stack) - 1])
        else:
            print(-1)
