import sys

people, party = list(map(int, sys.stdin.readline().strip().split(' ')))
truth_people = list(map(int, sys.stdin.readline().strip().split(' ')))[1:]
parent = [i for i in range(people + 1)]


def find_root(node):
    if parent[node] != node:
        parent[node] = find_root(parent[node])
    return parent[node]


def union(a, b):
    root_a = find_root(a)
    root_b = find_root(b)
    if a < b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


parties = []
for _ in range(party):
    count, *party_people = list(map(int, sys.stdin.readline().strip().split(' ')))
    parties.append(party_people)
    for i in range(count - 1):
        union(party_people[i], party_people[i + 1])

for i in range(1, people + 1):
    find_root(i)

ans = set()
for t in truth_people:
    if parent[t] == -1:
        continue
    temp = parent[t]
    for i in range(1, people + 1):
        if parent[i] == temp:
            ans.add(i)

answer = 0
for par in parties:
    if not ans & set(par):
        answer += 1

print(answer)
