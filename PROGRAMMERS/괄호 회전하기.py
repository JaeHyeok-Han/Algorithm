from collections import deque


def is_valid(arr):
    example = ['(', '{', '[']
    stack = []
    for ele in arr:
        if ele in example:
            stack.append(ele)
        elif ele == ')':
            if not stack:
                return False
            if stack[len(stack) - 1] == '(':
                stack.pop()
            else:
                return False
        elif ele == '}':
            if not stack:
                return False
            if stack[len(stack) - 1] == '{':
                stack.pop()
            else:
                return False
        elif ele == ']':
            if not stack:
                return False
            if stack[len(stack) - 1] == '[':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


def solution(s):
    answer = 0
    chars = deque(list(s))

    for i in range(len(s)):
        if i != 0:
            chars.rotate(-1)
        if is_valid(chars):
            answer += 1

    return answer
