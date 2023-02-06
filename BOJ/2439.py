import sys
count = int(sys.stdin.readline())
for i in range(count):
    print(' ' * (count - (i + 1)) + '*' * (i + 1))
    