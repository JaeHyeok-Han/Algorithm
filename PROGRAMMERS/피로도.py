def solution(k, dungeons):
    max_num = 0
    answer = 0
    hp = k
    visited = [False for _ in range(len(dungeons))]
    stack = []

    def dfs(n):
        stack.append(n)
        nonlocal hp, answer, max_num
        if hp >= dungeons[n][0]:
            visited[n] = True
            hp -= dungeons[n][1]
            answer += 1
            if answer > max_num:
                max_num = answer
            for index, is_visited in enumerate(visited):
                if not is_visited:
                    dfs(index)
            visited[n] = False
            hp += dungeons[n][1]
            answer -= 1

    for i in range(len(dungeons)):
        dfs(i)
    return max_num


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
