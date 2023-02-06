import sys
result = 1
for _ in range(3):
    result *= int(sys.stdin.readline())
number_count = [0 for _ in range(10)]
for number in list(str(result)):
    number_count[int(number)] += 1
for number in number_count:
    print(number)
