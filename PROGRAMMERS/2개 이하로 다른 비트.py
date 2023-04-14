def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
            continue
        temp = '0' + bin(num)[2:]
        idx = temp.rfind('0')
        temp = list(temp)
        temp[idx] = '1'
        temp[idx + 1] = '0'
        answer.append(int(''.join(temp), 2))

    return answer
