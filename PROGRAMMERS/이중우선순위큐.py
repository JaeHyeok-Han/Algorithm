from heapq import heappop, heappush


def solution(operations):
    visited = {}
    min_heap = []
    max_heap = []

    for command in operations:
        t, value = command.split(' ')
        value = int(value)
        if t == 'I':
            heappush(min_heap, value)
            heappush(max_heap, -value)
            if value in visited:
                visited[value] += 1
            else:
                visited[value] = 1
        else:
            if value == 1:
                while max_heap and visited[-max_heap[0]] == 0:
                    heappop(max_heap)
                if max_heap:
                    cur = -heappop(max_heap)
                    visited[cur] -= 1
            else:
                while min_heap and visited[min_heap[0]] == 0:
                    heappop(min_heap)
                if min_heap:
                    cur = heappop(min_heap)
                    visited[cur] -= 1
    answer = [i for i in visited if visited[i] != 0]
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]
