from heapq import heapify, heappop, heappush


def solution(ability, number):
    new_ability = ability
    heapify(ability)
    for _ in range(number):
        min1 = heappop(new_ability)
        min2 = heappop(new_ability)
        heappush(new_ability, min1 + min2)
        heappush(new_ability, min1 + min2)
    return sum(new_ability)


print(solution([10, 3, 7, 2], 2))
print(solution([1, 2, 3, 4], 3))
