import sys

type_count, target = list(map(int, sys.stdin.readline().strip().split(' ')))
coin_type = [int(sys.stdin.readline()) for _ in range(type_count)]
answer = 0
cur_type = type_count - 1
while target:
    if coin_type[cur_type] <= target:
        temp = target // coin_type[cur_type]
        target -= temp * coin_type[cur_type]
        answer += temp
    cur_type -= 1

print(answer)
