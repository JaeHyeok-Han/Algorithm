import sys

for _ in range(int(sys.stdin.readline())):
    clothes_type = {}
    answer = 1
    for _ in range(int(sys.stdin.readline())):
        name, position = sys.stdin.readline().strip().split(' ')
        if position in clothes_type:
            clothes_type[position] += 1
        else:
            clothes_type[position] = 1
    for i in clothes_type:
        answer *= (clothes_type[i] + 1)
    print(answer - 1)
    