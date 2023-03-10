import sys
from collections import Counter

N = int(sys.stdin.readline())
pages = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
answer = {
    -1: 0,
    0: 0,
    1: 0
}


def solution(lists):
    n = len(lists)
    if n == 1:
        answer[lists[0][0]] += 1
        return
    minus = 0
    zero = 0
    plus = 0
    for li in lists:
        for ele in li:
            if ele == -1:
                minus += 1
            elif ele == 0:
                zero += 1
            else:
                plus += 1
    if minus == n ** 2:
        answer[-1] += 1
    elif zero == n ** 2:
        answer[0] += 1
    elif plus == n ** 2:
        answer[1] += 1
    else:
        for i in range(3):
            temps = lists[i * (n // 3):(i + 1) * (n // 3)]
            for j in range(3):
                new_lists = []
                for temp in temps:
                    new_lists.append(temp[j * (n // 3):(j + 1) * (n // 3)])
                solution(new_lists)


solution(pages)
for ans in answer:
    print(answer[ans])