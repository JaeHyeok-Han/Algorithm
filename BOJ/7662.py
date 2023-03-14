import sys
from heapq import heappush, heappop

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    command_count = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    is_deleted = [False for _ in range(command_count)]
    for i in range(command_count):
        command, value = sys.stdin.readline().strip().split(' ')
        if command == 'I':
            heappush(min_heap, (int(value), i))
            heappush(max_heap, (int(value) * -1, i))
        else:
            if min_heap:
                if value == '1':
                    while max_heap and is_deleted[max_heap[0][1]]:
                        heappop(max_heap)
                    if max_heap:
                        is_deleted[max_heap[0][1]] = True
                        heappop(max_heap)
                else:
                    while min_heap and is_deleted[min_heap[0][1]]:
                        heappop(min_heap)
                    if min_heap:
                        is_deleted[min_heap[0][1]] = True
                        heappop(min_heap)
    while max_heap and is_deleted[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and is_deleted[min_heap[0][1]]:
        heappop(min_heap)
    if min_heap and max_heap:
        print(f'{max_heap[0][0] * -1} {min_heap[0][0]}')
    else:
        print('EMPTY')
