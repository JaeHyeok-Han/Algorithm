import sys

test_case_count = int(sys.stdin.readline())
for _ in range(test_case_count):
    arr = list(sys.stdin.readline().strip())
    stack = []
    flag = False
    for char in arr:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                flag = True
                break
    if not flag:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
