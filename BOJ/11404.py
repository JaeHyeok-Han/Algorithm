import sys

INF = 987654321
V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
edge = [[INF] * V for _ in range(V)]

for _ in range(E):
    s, e, w = list(map(int, sys.stdin.readline().strip().split(' ')))
    edge[s - 1][e - 1] = min(edge[s - 1][e - 1], w)

for i in range(V):
    edge[i][i] = 0
    for j in range(V):
        for k in range(V):
            edge[j][k] = min(edge[j][i] + edge[i][k], edge[j][k])

for line in edge:
    for num in line:
        if num == INF:
            print(0, end=' ')
        else:
            print(num, end=' ')
    print()
