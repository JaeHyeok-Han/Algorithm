from itertools import permutations


def check(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    n = len(numbers)
    temp = set()
    for i in range(1, n + 1):
        for l in list(permutations(numbers, i)):
            temp.add(int(''.join(l)))

    for n in temp:
        if check(n):
            answer += 1

    return answer
