import sys
from heapq import heappush

number = int(sys.stdin.readline())
numbers = []
for number in range(number):
    heappush(numbers, int(sys.stdin.readline()))
for number in numbers:
    print(number)
