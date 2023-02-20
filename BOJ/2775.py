import sys
test_case = int(sys.stdin.readline())
house = [[-1 for _ in range(15)] for _ in range(15)]


def get_people(k, n):
    if k == 0:
        return n
    if house[k][n] != -1:
        return house[k][n]
    else:
        total = 0
        for i in range(1, n + 1):
            total += get_people(k - 1, i)
        house[k][n] = total
        return total


for _ in range(test_case):
    floor = int(sys.stdin.readline())
    home = int(sys.stdin.readline())
    print(get_people(floor, home))
