from heapq import heappush, heappop

def solution(n, works):
    answer = 0
    queue = []
    while works:
        heappush(queue, -works.pop())
    while n:
        temp = -heappop(queue)
        if temp == 0:
            break
        heappush(queue, -(temp - 1))
        n -= 1
    for i in queue:
        answer += i ** 2
    return answer
