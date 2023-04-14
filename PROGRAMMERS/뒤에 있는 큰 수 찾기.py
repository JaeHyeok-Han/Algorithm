def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, num in enumerate(numbers):
        if not stack:
            stack.append([num, i])
        else:
            while stack and stack[len(stack) - 1][0] < num:
                cur, j = stack.pop()
                answer[j] = num
            stack.append([num, i])

    return answer
