import sys

a, b, c = list(map(int, sys.stdin.readline().strip().split(' ')))
visited = {
    1: a % c
}


def solution(n):
    if n in visited:
        return visited[n]
    else:
        m = n // 2
        visited[n] = (solution(m) * solution(n - m)) % c
        return visited[n]


print(solution(b))
