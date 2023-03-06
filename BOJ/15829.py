import sys

length = int(sys.stdin.readline())
chars = list(map(lambda x: ord(x) - 96, list(sys.stdin.readline().strip())))

answer = 0
for i, char in enumerate(chars):
    answer += (char * (31 ** i))

print(answer % 1234567891)
