def solution(food):
    answer = ''
    temp = ''
    for i, count in enumerate(food):
        if i == 0:
            continue
        cur = count
        if cur % 2 == 1:
            cur -= 1
        cur //= 2
        for j in range(cur):
            temp += str(i)
    answer += temp
    answer += '0'
    answer += temp[::-1]
    return answer
