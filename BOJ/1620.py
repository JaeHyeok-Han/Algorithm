import sys

N, Q = list(map(int, sys.stdin.readline().strip().split(' ')))
dogam_obj = {}
dogam_arr = ['']
for i in range(N):
    name = sys.stdin.readline().strip()
    dogam_obj[name] = i + 1
    dogam_arr.append(name)
for i in range(Q):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(dogam_arr[int(q)])
    else:
        print(dogam_obj[q])
