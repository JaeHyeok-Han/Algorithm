import sys

N = int(sys.stdin.readline())
num = 1
for i in range(1, N + 1):
    num *= i

c = 0
num_str = list(str(num))
while num_str:
    if num_str.pop() == '0':
        c += 1
    else:
        break

print(c)
