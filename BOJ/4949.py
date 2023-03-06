import sys

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    str_arr = list(string)
    stack = []
    flag = False
    for char in str_arr:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack:
                if stack[len(stack) - 1] == '(':
                    stack.pop()
                else:
                    print('no')
                    flag = True
                    break
            else:
                print('no')
                flag = True
                break
        elif char == ']':
            if stack:
                if stack[len(stack) - 1] == '[':
                    stack.pop()
                else:
                    print('no')
                    flag = True
                    break
            else:
                print('no')
                flag = True
                break
        else:
            continue
    if not flag:
        if stack:
            print('no')
        else:
            print('yes')
