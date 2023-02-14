import sys
from collections import deque
number = int(sys.stdin.readline())
numbers = deque([i + 1 for i in range(number)])

while len(numbers) != 1:
    numbers.popleft()
    numbers.append((numbers.popleft()))
print(numbers[0])
