from heapq import heappush, heappop


def solution(k, score):
    answer = []
    min_heap = []
    for s in score:
        if len(min_heap) < k:
            heappush(min_heap, s)
        else:
            if s > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, s)
        answer.append(min_heap[0])
    return answer
