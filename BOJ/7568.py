import sys

test_case_count = int(sys.stdin.readline())
info = []
for _ in range(test_case_count):
     info.append(list(map(int, sys.stdin.readline().strip().split(' '))))

for i, ele in enumerate(info):
    count = 0
    for j, el in enumerate(info):
        if i == j:
            continue
        if el[0] > ele[0] and el[1] > ele[1]:
            count += 1
    print(count + 1, end=' ')
