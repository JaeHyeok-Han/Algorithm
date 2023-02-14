import sys
test_case = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().strip().split(' ')))


def check(number):
    if number == 1:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


answer = 0
for num in numbers:
    if check(num):
        answer += 1
print(answer)
