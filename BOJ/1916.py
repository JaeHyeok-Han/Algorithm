import sys
from heapq import heappop, heappush

INF = 987654321
V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
edge = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = list(map(int, sys.stdin.readline().strip().split(' ')))
    edge[s].append([e, w])
start, target = list(map(int, sys.stdin.readline().strip().split(' ')))


def di(node):
    table = [INF] * (V + 1)
    table[node] = 0
    queue = []
    heappush(queue, (0, node))

    while queue:
        dist, cur = heappop(queue)
        if table[cur] < dist:
            continue
        for end, weight in edge[cur]:
            cost = dist + weight
            if cost < table[end]:
                table[end] = cost
                queue.append((cost, end))
    return table


answer = di(start)
print(answer[target])
