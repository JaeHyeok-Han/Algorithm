from collections import Counter


def solution(k, tangerine):
    answer = 0
    number = Counter(tangerine)
    num = [number[i] for i in number]
    num.sort(reverse=True)
    temp = 0
    for i in num:
        if temp + i < k:
            temp += i
            answer += 1
        else:
            break

    return answer + 1
