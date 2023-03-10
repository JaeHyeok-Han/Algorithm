import sys

n, k = list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n, k):
    answer = []
    people = [i + 1 for i in range(n)]
    fac = [1 for _ in range(21)]
    for i in range(2, 21):
        fac[i] = fac[i - 1] * i

    while n > 1:
        temp = 0
        for i in range(1, n + 1):
            if temp < k <= fac[n - 1] * i:
                now = people[i - 1]
                answer.append(now)
                people.remove(now)
                k -= fac[n - 1] * (i - 1)
                n -= 1
                break
            else:
                temp += fac[n - 1]
    answer.append(people[0])

    return answer


print(solution(n, k))
