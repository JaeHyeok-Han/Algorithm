import sys
count = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().strip().split(' ')))
m = max(scores)
answer = 0
for score in scores:
    answer += (score / m * 100)
print(answer / len(scores))
