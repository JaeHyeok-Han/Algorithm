def solution(s, e):
    visited = {}
    queue = [[s, 0]]
    visited[s] = True
    while queue:
        cur = queue.pop(0)
        if cur[0] == e:
            return cur[1]
        else:
            if cur[0] - 1 not in visited:
                queue.append([cur[0] - 1, cur[1] + 1])
                visited[cur[0] - 1] = True
            if cur[0] + 1 not in visited:
                queue.append([cur[0] + 1, cur[1] + 1])
                visited[cur[0] + 1] = True
            if cur[0] + 5 not in visited:
                queue.append([cur[0] + 5, cur[1] + 1])
                visited[cur[0] + 5] = True


print(solution(5, 14))
print(solution(8, 3))
