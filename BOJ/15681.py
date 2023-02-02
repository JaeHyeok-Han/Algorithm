import sys

sys.setrecursionlimit(1000000)
nodeCount, rootIndex, queryCount = list(map(int, sys.stdin.readline().split(' ')))
edgeInfo = []
queries = []
for _ in range(nodeCount - 1):
    edgeInfo.append(sys.stdin.readline())
for _ in range(queryCount):
    queries.append(int(sys.stdin.readline()))

tree = [[] for _ in range(nodeCount + 1)]
for edge in edgeInfo:
    v1, v2 = list(map(int, edge.split(' ')))
    tree[v1].append(v2)
    tree[v2].append(v1)

childCount = [1 for _ in range(nodeCount + 1)]


def dfs(parent, current):
    count = 1
    for i in range(len(tree[current])):
        if tree[current][i] != parent:
            count += dfs(current, tree[current][i])
    childCount[current] = count
    return count


dfs(0, rootIndex)
for query in queries:
    print(childCount[query])
