def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score) >= m:
        for i in range(m - 1):
            score.pop()
        s = score.pop()
        answer += (s * m)
    return answer
