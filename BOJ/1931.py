import sys

N = int(sys.stdin.readline())
time_arr = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
time_arr.sort(key=lambda x: (x[1], x[0]))
cur = 0
answer = 0
for time in time_arr:
    if time[0] >= cur:
        cur = time[1]
        answer += 1
print(answer)
