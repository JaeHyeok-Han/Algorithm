queryCount = int(input())
queries = []
for _ in range(queryCount):
    queries.append(input())

for i, query in enumerate(queries):
    answer = 0
    brackets = list(query)
    stack = []
    count = 0
    for bracket in brackets:
        if bracket == '(':
            count += 1
        else:
            if stack[len(stack) - 1] == '(':
                count -= 1
                answer += count
            else:
                count -= 1
                answer += 1
        stack.append(bracket)
    print(f'#{i + 1}', answer)
