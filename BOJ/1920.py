import sys
_ = sys.stdin.readline()
targets = list(map(int, sys.stdin.readline().strip().split(' ')))
t = {}
_ = sys.stdin.readline()
numbers = list(map(int, sys.stdin.readline().strip().split(' ')))
for target in targets:
    if target not in t:
        t[target] = 1
    else:
        t[target] += 1
for number in numbers:
    if number in t:
        print(1)
    else:
        print(0)
