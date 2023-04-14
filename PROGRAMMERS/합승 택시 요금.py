def solution(n, s, a, b, fares):
    INF = 987654321
    edges = [[INF] * (n) for _ in range(n)]
    for start, end, weight in fares:
        edges[start - 1][end - 1] = weight
        edges[end - 1][start - 1] = weight
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j == k:
                    edges[j][k] = 0
                    continue
                if edges[j][k] > edges[j][i] + edges[i][k]:
                    edges[j][k] = edges[j][i] + edges[i][k]

    answer = INF
    for i in range(n):
        temp = edges[s - 1][i]
        temp += edges[i][a - 1]
        temp += edges[i][b - 1]
        if temp < answer:
            answer = temp

    return answer
