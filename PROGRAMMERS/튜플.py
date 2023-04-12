from collections import deque


def solution(s):
    answer = []
    queue = deque(list(s))
    queue.pop()
    queue.pop()
    queue.popleft()
    queue.popleft()
    new_str = ''
    while queue:
        new_str += queue.popleft()
    str_list = new_str.split('},{')
    str_list.sort(key=lambda x: (len(x)))
    for i, ele in enumerate(str_list):
        str_list[i] = set(map(int, str_list[i].split(',')))
        answer.append(*(str_list[i] - set(answer)))
    return answer
