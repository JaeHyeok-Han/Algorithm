def solution(menu, order, k):
    answer = 0
    time_table = []
    make_table = []
    make_time = 0
    for i, drink in enumerate(order):
        if i * k + menu[drink] >= make_time + menu[drink]:
            make_time = i * k + menu[drink]
            make_table.append(make_time)
            time_table.append(make_time)
        else:
            make_time += menu[drink]
            make_table.append(make_time)
            time_table.append(make_time)

    for i in range(len(order)):
        a = i + 1 - len(list(filter(lambda x: x <= i * k, time_table)))
        if a >= answer:
            answer = a
    return answer


print(solution([5, 12, 30], [1, 2, 0, 1], 10))
print(solution([5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10))
print(solution([5], [0, 0, 0, 0, 0], 5))
