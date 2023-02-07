import sys
target_n = int(sys.stdin.readline())
number = 665
n = 0
while True:
    if '666' in str(number):
        n += 1
        if n == target_n:
            print(number)
            break
    number += 1
