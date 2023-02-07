import sys

b_board = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
w_board = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
minimum = 987654321

n, m = list(map(int, sys.stdin.readline().strip().split(' ')))
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

for i in range(n - 7):
    for j in range(m - 7):
        b_diff = 0
        w_diff = 0
        for k in range(8):
            for l in range(8):
                if board[i + k][j + l] != b_board[k][l]:
                    b_diff += 1
                if board[i + k][j + l] != w_board[k][l]:
                    w_diff += 1
        minimum = min([minimum, b_diff, w_diff])
print(minimum)
