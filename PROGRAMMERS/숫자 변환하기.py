from collections import deque

def solution(x, y, n):
    queue = deque([x])
    visited = {
        x: 0
    }
    while queue:
        cur = queue.popleft()
        if cur == y:
            return visited[cur]
        for i in [cur + n, cur * 2, cur * 3]:
            if i <= y and i not in visited:
                visited[i] = visited[cur] + 1
                queue.append(i)
    return -1
