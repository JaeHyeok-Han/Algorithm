import string

tmp = string.digits + string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def is_valid(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    arr = str(convert(n, k)).split('0')
    for i in arr:
        if len(i) != 0:
            if is_valid(int(i)):
                answer += 1

    return answer