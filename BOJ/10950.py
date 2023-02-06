import sys
for _ in range(int(sys.stdin.readline())):
    num1, num2 = list(map(int, sys.stdin.readline().strip().split(' ')))
    print(num1 + num2)
