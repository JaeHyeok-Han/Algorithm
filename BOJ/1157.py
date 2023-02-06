import sys
str = sys.stdin.readline().strip().upper()
count = {}
for char in str:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
m = 0
for char in count:
    if count[char] >= m:
        m = count[char]
answer = ''
for char in count:
    if count[char] == m:
        answer += char

print('?' if len(answer) > 1 else answer)
