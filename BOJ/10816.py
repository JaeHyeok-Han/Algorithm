import sys

card_count = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().strip().split(' ')))
target_count = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().strip().split(' ')))
answer = {}

for card in cards:
    if card in answer:
        answer[card] += 1
    else:
        answer[card] = 1

for target in targets:
    if target in answer:
        print(answer[target], end=' ')
    else:
        print(0, end=' ')
        