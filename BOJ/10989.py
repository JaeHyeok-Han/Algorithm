import sys

number = int(sys.stdin.readline())
numbers = [0] * 10001
for _ in range(number):
    numbers[int(sys.stdin.readline())] += 1
for i in range(10001):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)
