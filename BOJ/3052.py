import sys
numbers = []
for _ in range(10):
    numbers.append(int(sys.stdin.readline()) % 42)
print(len(set(numbers)))
