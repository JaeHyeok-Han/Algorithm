import sys
import math

target = int(sys.stdin.readline())

five = 0
answer = 987654321
flag = False

while five <= (math.ceil(target / 5)):
    three = (target - (five * 5)) / 3
    if three == int(three) and three >= 0:
        flag = True
        temp = int(three) + five
        if temp < answer:
            answer = temp
        five += 1
    else:
        five += 1

if flag:
    print(answer)
else:
    print(-1)
