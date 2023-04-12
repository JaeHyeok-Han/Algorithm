from collections import deque


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:
        cur = goal.popleft()
        if cards1:
            c1 = cards1.popleft()
            if c1 == cur:
                continue
            else:
                cards1.appendleft(c1)
        if cards2:
            c2 = cards2.popleft()
            if c2 == cur:
                continue
            else:
                cards2.appendleft(c2)
        goal.appendleft(cur)
        break

    if goal:
        return 'No'
    else:
        return 'Yes'
