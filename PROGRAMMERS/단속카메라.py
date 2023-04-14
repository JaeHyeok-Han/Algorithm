def solution(routes):
    answer = 1
    routes.sort(key=lambda x: (x[1], x[0]))
    print(routes)
    cur = routes[0][1]
    for i, info in enumerate(routes):
        if i == 0:
            continue
        if info[0] <= cur:
            continue
        else:
            answer += 1
            cur = info[1]

    return answer
