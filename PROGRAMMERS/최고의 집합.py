def solution(n, s):
    answer = []
    while n > 1:
        t = s // n
        if t == 0:
            return [-1]
        answer.append(t)
        n -= 1
        s -= t
    if s == 0:
        return [-1]
    else:
        answer.append(s)
        answer.sort()
        return answer
