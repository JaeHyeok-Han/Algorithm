import sys
from heapq import heappush, heappop

N, E = list(map(int, sys.stdin.readline().strip().split(' ')))
edge = [[] for _ in range((N + 1))]
for _ in range(E):
    start, end, weight = list(map(int, sys.stdin.readline().strip().split(' ')))
    edge[start].append([end, weight])
    edge[end].append([start, weight])
point1, point2 = list(map(int, sys.stdin.readline().strip().split(' ')))


def di(s, target):
    q = []
    heappush(q, (0, s))
    table = [987654321] * (N + 1)
    table[s] = 0
    while q:
        dist, now = heappop(q)
        if table[now] < dist:
            continue
        for e, w in edge[now]:
            cost = dist + w
            if cost < table[e]:
                table[e] = cost
                heappush(q, (cost, e))
    if table[target] == 987654321:
        return -1
    else:
        return table[target]


if di(1, point1) != -1 and di(point1, point2) != -1 and di(point2, N) != -1:
    answer1 = di(1, point1) + di(point1, point2) + di(point2, N)
else:
    answer1 = 987654321

if di(1, point2) != -1 and di(point2, point1) != -1 and di(point1, N) != -1:
    answer2 = di(1, point2) + di(point2, point1) + di(point1, N)
else:
    answer2 = 987654321

if answer1 == 987654321 and answer2 == 987654321:
    print(-1)
else:
    print(min(answer1, answer2))
