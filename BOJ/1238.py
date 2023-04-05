import sys
from heapq import heappop, heappush

INF = 987654321
N, M, X = list(map(int, sys.stdin.readline().strip().split(' ')))
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, weight = list(map(int, sys.stdin.readline().strip().split(' ')))
    edges[start].append([end, weight])


def di(node):
    table = [INF] * (N + 1)
    table[node] = 0
    queue = []
    heappush(queue, (0, node))
    while queue:
        wei, cur = heappop(queue)
        if table[cur] < wei:
            continue
        for ne, we in edges[cur]:
            cost = wei + we
            if cost < table[ne]:
                table[ne] = cost
                heappush(queue, (cost, ne))
    return table


answer = 0
back_cost = di(X)
for i in range(1, N + 1):
    if i == X:
        continue
    result = di(i)
    temp = result[X] + back_cost[i]
    if temp > answer:
        answer = temp

print(answer)
