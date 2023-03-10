import sys

test_case = int(sys.stdin.readline())
memo = [-1 for _ in range(12)]
memo[1] = 1
memo[2] = 2
memo[3] = 4


def solution(num):
    if memo[num] != -1:
        return memo[num]
    else:
        memo[num] = solution(num - 1) + solution(num - 2) + solution(num - 3)
        return memo[num]


for _ in range(test_case):
    print(solution(int(sys.stdin.readline())))
