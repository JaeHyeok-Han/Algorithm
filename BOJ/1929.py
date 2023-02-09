import sys
M, N = list(map(int, sys.stdin.readline().strip().split(' ')))


def check(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for number in range(M, N + 1):
    if number == 1:
        continue
    elif number == 2 or number == 3:
        print(number)
    elif number % 2 == 0 or number % 3 == 0:
        continue
    else:
        if check(number):
            print(number)
        else:
            continue
