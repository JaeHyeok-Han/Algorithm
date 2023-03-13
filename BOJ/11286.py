import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num:
        heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
