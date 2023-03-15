import sys

N = int(sys.stdin.readline())
visited = [0, 1]

for i in range(2, 50001):
    min_value = 987654321
    j = 1
    while (j ** 2) <= i:
        min_value = min(min_value, visited[i - (j ** 2)])
        j += 1
    visited.append(min_value + 1)

print(visited[N])
