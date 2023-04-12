def solution(prices):
    answer = [-1] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and stack[len(stack) - 1][0] > price:
            temp = stack.pop()
            answer[temp[1]] = i - temp[1]
        stack.append([price, i])
    while stack:
        temp = stack.pop()
        answer[temp[1]] = (len(prices) - 1) - temp[1]
    return answer
