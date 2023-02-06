import sys
while True:
    try:
        num1, num2 = list(map(int, sys.stdin.readline().strip().split(' ')))
        print(num1 + num2)
    except:
        break