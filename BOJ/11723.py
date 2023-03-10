import sys

M = int(sys.stdin.readline())
all_nums = set([str(i + 1) for i in range(20)])
nums = set()
for _ in range(M):
    command = sys.stdin.readline().strip().split(' ')
    if command[0] == 'add':
        nums.add(command[1])
    elif command[0] == 'remove':
        if command[1] in nums:
            nums.remove(command[1])
    elif command[0] == 'check':
        print(1 if command[1] in nums else 0)
    elif command[0] == 'toggle':
        if command[1] in nums:
            nums.remove(command[1])
        else:
            nums.add(command[1])
    elif command[0] == 'all':
        nums = all_nums
    else:
        nums.clear()
