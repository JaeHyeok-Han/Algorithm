import sys
numbers = []
for _ in range(9):
    numbers.append(int(sys.stdin.readline()))
m = max(numbers)
m_index = numbers.index(m) + 1
print(m, m_index)
