import sys


def gcm(n, m):
    if m > n:
        n, m = m, n
    while m != 0:
        n, m = m, n % m
    return n


def solution(input_list):
    n, m, target_x, target_y = input_list
    lcm_nm = n * m // gcm(n, m)
    n_arr = []
    while target_x <= lcm_nm:
        n_arr.append(target_x)
        target_x += n
    m_arr = []
    while target_y <= lcm_nm:
        m_arr.append(target_y)
        target_y += m
    arr = list(set(n_arr) & set(m_arr))
    if arr:
        return arr[0]
    else:
        return -1


for _ in range(int(sys.stdin.readline())):
    print(solution(list(map(int, sys.stdin.readline().strip().split(' ')))))
