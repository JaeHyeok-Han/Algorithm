import sys
N = int(sys.stdin.readline().strip())
input_numbers = []
reverse_stacks = []
original_stacks = []
commands = []
for _ in range(N):
    input_numbers.append(int(sys.stdin.readline().strip()))
while input_numbers:
    if not reverse_stacks:
        commands.append('-')
        reverse_stacks.append(input_numbers.pop())
    elif reverse_stacks[len(reverse_stacks) - 1] < input_numbers[len(input_numbers) - 1]:
        commands.append('-')
        reverse_stacks.append(input_numbers.pop())
    else:
        commands.append('+')
        original_stacks.append(reverse_stacks.pop())
while reverse_stacks:
    commands.append('+')
    original_stacks.append(reverse_stacks.pop())
is_sorted = all(x > y for x, y in zip(original_stacks[:-1], original_stacks[1:]))
if is_sorted:
    for command in commands[::-1]:
        print(command)
else:
    print('NO')
