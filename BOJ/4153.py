import sys

while True:
    arr = list(map(int, sys.stdin.readline().strip().split(' ')))
    arr.sort()
    a, b, c = arr
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a ** 2 + b ** 2 == c ** 2:
            print('right')
        else:
            print('wrong')
