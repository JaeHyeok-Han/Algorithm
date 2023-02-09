import sys
target_number = int(sys.stdin.readline())
n = 0


def check(number):
    answer = number
    for num in str(number):
        answer += int(num)
    return answer


while True:
    if n > 1000000:
        print(0)
        break
    if check(n) == target_number:
        print(n)
        break
    else:
        n += 1
