import sys

string = sys.stdin.readline().strip()
temp = ''
math_arr = []
for s in string:
    if s.isdigit():
        temp += s
    else:
        math_arr.append(int(temp))
        math_arr.append(s)
        temp = ''
math_arr.append(int(temp))

mode = 0
answer = 0
for num in math_arr:
    if num == '-':
        mode = 1
    elif num == '+':
        pass
    else:
        if not mode:
            answer += num
        else:
            answer -= num

print(answer)
