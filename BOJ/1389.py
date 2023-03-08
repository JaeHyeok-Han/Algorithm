import sys
from collections import deque

n, e = list(map(int, sys.stdin.readline().strip().split(' ')))
edge = {}
for _ in range(e):
    n1, n2 = list(map(int, sys.stdin.readline().strip().split(' ')))
    if n1 in edge:
        edge[n1].append(n2)
    else:
        edge[n1] = [n2]
    if n2 in edge:
        edge[n2].append(n1)
    else:
        edge[n2] = [n1]
for i in edge:
    edge[i].sort()


def bfs(s):
    answer = 0
    queue = deque()
    queue.append((s, 0))
    visited = [s]
    while queue:
        cur, count = queue.popleft()
        for ele in edge[cur]:
            if ele not in visited:
                answer += count + 1
                queue.append((ele, count + 1))
                visited.append(ele)
        count += 1
    return answer


answers = {}
for i in edge:
    answers[i] = bfs(i)
m = answers[min(answers, key=answers.get)]
print(min([i for i in edge if answers[i] == m]))
