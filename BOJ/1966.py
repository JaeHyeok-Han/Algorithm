import sys
from collections import deque
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    count_of_doc, target = list(map(int, sys.stdin.readline().strip().split(' ')))
    temps = list(map(int, sys.stdin.readline().strip().split(' ')))
    docs = deque()
    for idx, temp in enumerate(temps):
        docs.append({
            'index': idx,
            'priority': temp
        })
    count = 0
    temps.sort()
    while docs:
        cur = docs.popleft()
        if cur['priority'] == temps[len(temps) - 1]:
            count += 1
            temps.pop()
            if cur['index'] == target:
                print(count)
                break
        else:
            docs.append(cur)
