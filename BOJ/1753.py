import sys
from heapq import heappop, heappush

INF = 987654321
V, E = list(map(int, sys.stdin.readline().strip().split(' ')))
edge = [[] for _ in range(V + 1)]
start = int(sys.stdin.readline())
for _ in range(E):
    s, e, w = list(map(int, sys.stdin.readline().strip().split(' ')))
    edge[s].append([w, e])


def di(node):
    table = [INF for _ in range(V + 1)]
    table[node] = 0
    heap = []
    heappush(heap, (0, node))
    while heap:
        dist, cur = heappop(heap)
        for w, e in edge[cur]:
            cost = dist + w
            if table[e] < cost:
                continue
            table[e] = cost
            heappush(heap, (cost, e))
    return table


answer = di(start)
for i in range(1, V + 1):
    if answer[i] == INF:
        print('INF')
    else:
        print(answer[i])
