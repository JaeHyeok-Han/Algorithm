import sys
from collections import deque

test_case = int(sys.stdin.readline())
for i in range(test_case):
    order = deque()
    b_order = deque()
    o_order = deque()

    command = deque(sys.stdin.readline().strip().split(' '))
    n = command.popleft()
    while command:
        robot = command.popleft()
        value = command.popleft()
        order.append((robot, int(value)))
        if robot == 'B':
            b_order.append(int(value))
        else:
            o_order.append(int(value))

    answer = 0
    b, o = 1, 1
    for robot, value in order:
        if robot == 'B':
            while b != value:
                if b < value:
                    b += 1
                else:
                    b -= 1
                if o_order and o < o_order[0]:
                    o += 1
                elif o_order and o > o_order[0]:
                    o -= 1
                answer += 1
            b_order.popleft()
            if o_order and o < o_order[0]:
                o += 1
            elif o_order and o > o_order[0]:
                o -= 1
            answer += 1
        else:
            while o != value:
                if o < value:
                    o += 1
                else:
                    o -= 1
                if b_order and b < b_order[0]:
                    b += 1
                elif b_order and b > b_order[0]:
                    b -= 1
                answer += 1
            o_order.popleft()
            if b_order and b < b_order[0]:
                b += 1
            elif b_order and b > b_order[0]:
                b -= 1
            answer += 1
    print(f'{i + 1} {answer}')
