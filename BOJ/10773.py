import sys

test_case_count = int(sys.stdin.readline())
arr = []
for _ in range(test_case_count):
    num = int(sys.stdin.readline())
    if num:
        arr.append(num)
    else:
        arr.pop()
print(sum(arr))
