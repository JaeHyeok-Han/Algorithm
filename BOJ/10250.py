import sys
from math import ceil

test_case_count = int(sys.stdin.readline())
for _ in range(test_case_count):
    h, w, n = list(map(int, sys.stdin.readline().strip().split(" ")))
    room = ceil(n / h)
    room = '0' + str(room) if room < 10 else room
    print(f'{h if n % h == 0 else n % h}{room}')
