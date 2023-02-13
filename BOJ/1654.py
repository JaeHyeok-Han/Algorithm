import sys
count_of_lan, target_number = list(map(int, sys.stdin.readline().strip().split(' ')))
lan_lengths = []
for _ in range(count_of_lan):
    lan_lengths.append(int(sys.stdin.readline().strip()))

pre = max(lan_lengths)
answer = 1
while answer <= pre:
    print(answer, pre)
    count = 0
    mid = (pre + answer) // 2
    for length in lan_lengths:
        count += length // mid
    if count < target_number:
        pre = mid - 1
    else:
        answer = mid + 1
print(pre)
