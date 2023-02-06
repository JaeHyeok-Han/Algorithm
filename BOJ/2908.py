import sys
num1, num2 = sys.stdin.readline().strip().split(' ')
num1 = num1[::-1]
num2 = num2[::-1]
print(num1 if num1 > num2 else num2)
