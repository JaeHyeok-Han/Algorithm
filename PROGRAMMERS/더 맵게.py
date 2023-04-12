from heapq import heappush, heappop


def solution(scoville, K):
    answer = 0
    queue = []
    for food in scoville:
        heappush(queue, food)
    while len(queue) > 1:
        if queue[0] >= K:
            break
        first = heappop(queue)
        second = heappop(queue)
        heappush(queue, first + second * 2)
        answer += 1

    if queue[0] >= K:
        return answer
    else:
        return -1
