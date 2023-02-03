def solution(n):
    answer = n + 1
    count_of_one = bin(n)[2:].count('1')
    while True:
        if bin(answer)[2:].count('1') == count_of_one:
            break;
        else:
            answer += 1

    return answer


print(solution(78))
print(solution(15))
