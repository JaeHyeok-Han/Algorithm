import sys
from collections import deque
command_count = int(sys.stdin.readline())
queue = deque()
for _ in range(command_count):
    command = sys.stdin.readline().strip().split(' ')
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            ele = queue.popleft()
            print(ele)
            queue.appendleft(ele)
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            ele = queue.pop()
            print(ele)
            queue.append(ele)
