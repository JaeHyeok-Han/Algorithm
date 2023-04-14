def check(m, n, game_map):
    count = 0
    result = [[0] * m for _ in range(n)]
    for i in range(n - 1):
        for j in range(m - 1):
            if game_map[i][j] == -1:
                continue
            if game_map[i][j] == game_map[i][j + 1] == game_map[i + 1][j] == game_map[i + 1][j + 1]:
                result[i][j] = 1
                result[i][j + 1] = 1
                result[i + 1][j] = 1
                result[i + 1][j + 1] = 1
    for i in range(n):
        for j in range(m):
            if result[i][j]:
                game_map[i][j] = -1
                count += 1
    return (game_map, count)


def solution(m, n, board):
    answer = 0
    game_map = [[' '] * m for _ in range(n)]
    for i in range(m):
        for j, char in enumerate(list(board[m - i - 1])):
            game_map[j][i] = char
    while True:
        game_map, count = check(m, n, game_map)
        if count == 0:
            break
        for i, line in enumerate(game_map):
            game_map[i] = [char for char in line if char != -1]
            while len(game_map[i]) < m:
                game_map[i].append(-1)

    for i in range(n):
        for j in range(m):
            if game_map[i][j] == -1:
                answer += 1

    return answer
