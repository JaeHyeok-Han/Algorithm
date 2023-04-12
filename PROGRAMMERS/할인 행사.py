def solution(want, number, discount):
    answer = 0
    target = {}
    for i, obj in enumerate(want):
        target[obj] = number[i]
    check = {}
    for i, obj in enumerate(discount):
        if obj in check:
            check[obj] += 1
        else:
            check[obj] = 1
        if i >= 10:
            n = discount[i - 10]
            check[n] -= 1
            if check[n] == 0:
                del check[n]
        if check == target:
            answer += 1

    return answer
