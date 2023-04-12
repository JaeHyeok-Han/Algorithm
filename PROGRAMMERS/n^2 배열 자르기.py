def solution(n, left, right):
    answer = []
    sx = (left // n) + 1
    sy = (left % n) + 1
    ex = (right // n) + 1
    ey = (right % n) + 1
    if sx == ex:
        for i in range(sy, ey + 1):
            answer.append(max(sx, i))
        return answer
    for i in range(sx, ex + 1):
        for j in range(1, n + 1):
            if i == sx:
                if j >= sy:
                    answer.append(max(i, j))
            elif i == ex:
                if j <= ey:
                    answer.append(max(i, j))
            else:
                answer.append(max(i, j))
    return answer
