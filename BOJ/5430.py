import sys
from collections import deque

test_case_count = int(sys.stdin.readline())
for _ in range(test_case_count):
    command_arr = sys.stdin.readline().strip().replace('RR', '')
    _ = int(sys.stdin.readline())
    num_str = sys.stdin.readline().strip().replace('[', '').replace(']', '')
    num_arr = deque() if len(num_str) == 0 else deque(num_str.split(','))

    mode = True
    for command in command_arr:
        if command == 'R':
            mode = False if mode else True
        else:
            if not num_arr:
                num_arr = 'error'
                break
            else:
                if mode:
                    num_arr.popleft()
                else:
                    num_arr.pop()

    if num_arr == 'error':
        print(num_arr)
    else:
        print("[", end='')
        if mode:
            print(','.join(num_arr), end='')
        else:
            num_arr.reverse()
            print(','.join(num_arr), end='')
        print("]")
