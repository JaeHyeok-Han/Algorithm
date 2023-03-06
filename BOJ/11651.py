import sys

test_case_count = int(sys.stdin.readline())
arr = []
for _ in range(test_case_count):
    arr.append(list(map(int, sys.stdin.readline().strip().split(' '))))

arr.sort(key=lambda x: (x[1], x[0]))
for ele in arr:
    print(f'{ele[0]} {ele[1]}')
