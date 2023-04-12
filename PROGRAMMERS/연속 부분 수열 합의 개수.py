def solution(elements):
    new_arr = elements * 2
    answer = set()
    max_length = len(elements)
    for i in range(1, max_length + 1):
        for j in range(max_length):
            answer.add(sum(new_arr[j:j+i]))
    return len(answer)
