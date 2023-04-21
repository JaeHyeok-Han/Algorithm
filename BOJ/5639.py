import sys
sys.setrecursionlimit(1000000)

nums = []
while True:
    try:
        num = int(sys.stdin.readline())
        nums.append(num)
    except:
        break

root = nums[0]
tree = {
    root: [-1, -1, -1]
}
stack = [root]

for num in nums:
    parent = stack[len(stack) - 1]
    if num < parent:
        stack.append(num)
        tree[parent][1] = num
        tree[num] = [parent, -1, -1]
    else:
        while stack and stack[len(stack) - 1] < num:
            parent = stack.pop()
        stack.append(num)
        tree[parent][2] = num
        tree[num] = [parent, -1, -1]


def post_order(value):
    if tree[value][1] != -1:
        post_order(tree[value][1])
    if tree[value][2] != -1:
        post_order(tree[value][2])
    print(value)


post_order(root)
