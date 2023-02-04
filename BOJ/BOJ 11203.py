import sys
input_line = sys.stdin.readline().strip().split(' ')
depth = int(input_line[0])

full_number = 2 ** (int(depth) + 1)
cur = 1
if len(input_line) > 1:
    for command in input_line[1]:
        cur *= 2
        if command == 'R':
            cur += 1
print(full_number - cur)
