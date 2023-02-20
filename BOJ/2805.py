from sys import stdin
num, target = list(map(int, stdin.readline().strip().split(' ')))
numbers = list(map(int, stdin.readline().strip().split(' ')))
left = 0
right = max(numbers)
result = 0
while left <= right:
    mid = (left + right) // 2
    total = 0
    for number in numbers:
        total += number - mid if number >= mid else 0
    if total < target:
        right = mid - 1
    else:
        result = mid
        left = mid + 1
print(result)
