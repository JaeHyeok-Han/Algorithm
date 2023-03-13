import sys

N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
no_hear = set()
no_see = set()
for _ in range(N):
    no_hear.add(sys.stdin.readline().strip())
for _ in range(M):
    no_see.add(sys.stdin.readline().strip())
no_people = list(no_hear & no_see)
print(len(no_people))
no_people.sort()
for people in no_people:
    print(people)
