from collections import deque


def solution(people, limit):
    people.sort()
    queue = deque(people)
    answer = 0
    while queue:
        if len(queue) == 1:
            answer += 1
            break
        start = queue.popleft()
        end = queue.pop()
        if start + end <= limit:
            answer += 1
        else:
            queue.appendleft(start)
            answer += 1

    return answer
