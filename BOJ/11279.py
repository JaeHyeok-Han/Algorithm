import sys
from heapq import heappush, heappop

command_count = int(sys.stdin.readline())
heap = []
for _ in range(command_count):
    command = int(sys.stdin.readline())
    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap) * -1)
    else:
        heappush(heap, command * -1)
