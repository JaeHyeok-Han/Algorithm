import sys

total, test = list(map(int, sys.stdin.readline().strip().split(' ')))
pw_book = {}
for _ in range(total):
    site, pw = sys.stdin.readline().strip().split(' ')
    pw_book[site] = pw
for _ in range(test):
    site = sys.stdin.readline().strip()
    print(pw_book[site])
