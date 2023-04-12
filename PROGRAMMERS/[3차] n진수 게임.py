import string

tmp = string.digits + string.ascii_uppercase


def convert(num, n):
    div, mod = divmod(num, n)
    if div == 0:
        return tmp[mod]
    else:
        return convert(div, n) + tmp[mod]


def solution(n, t, m, p):
    answer = ''
    result = []
    i = 0
    while len(result) < p + t * m:
        temp = convert(i, n)
        result += list(temp)
        i += 1

    while len(answer) < t:
        answer += result[p - 1]
        p += m
    return answer
