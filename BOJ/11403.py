import sys

N = int(sys.stdin.readline())
ground = []
for _ in range(N):
    ground.append(list(map(int, sys.stdin.readline().strip().split(' '))))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if ground[i][k] and ground[k][j]:
                ground[i][j] = 1

for i in range(N):
    for j in range(N):
        print(ground[i][j], end=' ')
    print()
