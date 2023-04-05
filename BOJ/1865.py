import sys

INF = 987654321
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    V, E, W = list(map(int, sys.stdin.readline().strip().split(' ')))
    edge = [[INF] * (V + 1) for _ in range(V + 1)]
    h = {}
    for _ in range(E):
        node1, node2, weight = list(map(int, sys.stdin.readline().strip().split(' ')))
        if weight < edge[node1][node2]:
            edge[node1][node2] = weight
            edge[node2][node1] = weight
    for _ in range(W):
        node1, node2, weight = list(map(int, sys.stdin.readline().strip().split(' ')))
        if node1 not in h:
            h[node1] = True
        if -weight < edge[node1][node2]:
            edge[node1][node2] = -weight
    edge_list = []
    for i in range(V + 1):
        for j in range(V + 1):
            if edge[i][j] != INF:
                edge_list.append((i, j, edge[i][j]))

    def bf(start):
        table = [INF] * (V + 1)
        table[start] = 0
        for count in range(V):
            for cur, ne, wei in edge_list:
                if table[cur] != INF and table[ne] > table[cur] + wei:
                    table[ne] = table[cur] + wei
                    if count == V - 1:
                        return True
        return False

    flag = False
    for i in h:
        if bf(i):
            flag = True
            break
    if flag:
        print('YES')
    else:
        print('NO')


