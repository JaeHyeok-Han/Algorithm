import sys
from collections import deque

command_count = int(sys.stdin.readline())
deq = deque()
for _ in range(command_count):
    input_str = sys.stdin.readline().strip().split(' ')
    command = input_str[0]
    if command == 'push_front':
        deq.appendleft(int(input_str[1]))
    elif command == 'push_back':
        deq.append(int(input_str[1]))
    elif command == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif command == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(deq))
    elif command == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if deq:
            temp = deq.popleft()
            print(temp)
            deq.appendleft(temp)
        else:
            print(-1)
    else:
        if deq:
            temp = deq.pop()
            print(temp)
            deq.append(temp)
        else:
            print(-1)
