import sys
number = int(sys.stdin.readline())
numbers = []
for number in range(number):
    numbers.append(list(map(int, sys.stdin.readline().strip().split(' '))))
numbers.sort(key=lambda x: (x[0], x[1]))
for number in numbers:
    print(number[0], number[1])
    