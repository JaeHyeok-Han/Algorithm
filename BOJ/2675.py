import sys
for _ in range(int(sys.stdin.readline())):
    count, str = list(sys.stdin.readline().strip().split(' '))
    answer = ''
    for char in str:
        answer += char * int(count)
    print(answer)
