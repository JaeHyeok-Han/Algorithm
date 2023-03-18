import sys
from collections import deque


def normalization(value):
    temp = str(value)
    if value < 1000:
        return '0' * (4 - len(temp)) + temp
    else:
        return temp


for _ in range(int(sys.stdin.readline())):
    init, target = list(map(int, sys.stdin.readline().strip().split(' ')))
    queue = deque()
    visited = {}
    queue.append(init)
    visited[init] = ''
    while queue:
        num = queue.popleft()
        if num == target:
            print(visited[num])
            break
        else:
            t = normalization(num)
            dslr = [((num * 2) % 10000, 'D'),
                    (9999 if num == 0 else num - 1, 'S'),
                    (int(t[1:4] + t[0]), 'L'),
                    (int(t[3] + t[0:3]), 'R')]
            for val, c in dslr:
                if val not in visited:
                    visited[val] = visited[num] + c
                    queue.append(val)
