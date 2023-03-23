import sys
from collections import deque

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
queue = deque()
for _ in range(N - 1):
    node1, node2 = list(map(int, sys.stdin.readline().strip().split(' ')))
    tree[node1].append(node2)
    tree[node2].append(node1)

queue.append(1)
while queue:
    cur = queue.popleft()
    child = tree[cur]
    for c in child:
        if parent[c] == 0:
            parent[c] = cur
            queue.append(c)

for i in range(2, N + 1):
    print(parent[i])
