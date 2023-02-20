import sys
number = int(sys.stdin.readline())
count = 0
target = 1
while True:
    target += (6 * count)
    if number <= target:
        break
    else:
        count += 1
print(count + 1)
