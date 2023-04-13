def solution(dirs):
    answer = 0
    direction = {
        'U': [0, 1],
        'R': [1, 0],
        'D': [0, -1],
        'L': [-1, 0],
    }
    visited = {}
    x, y = 0, 0
    for d in dirs:
        n_x = x + direction[d][0]
        n_y = y + direction[d][1]
        if -5 <= n_x <= 5 and -5 <= n_y <= 5:
            temp = str(x) + str(y) + str(n_x) + str(n_y)
            temp2 = str(n_x) + str(n_y) + str(x) + str(y)
            x = n_x
            y = n_y
            if temp not in visited and temp2 not in visited:
                visited[temp] = 1
                visited[temp2] = 1
                answer += 1
    return answer
