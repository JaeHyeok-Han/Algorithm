import sys
for _ in range(int(sys.stdin.readline())):
    str = sys.stdin.readline().strip()
    answer = 0
    count = 0
    for char in str:
        if char == 'O':
            count += 1
            answer += count
        else:
            count = 0
    print(answer)
