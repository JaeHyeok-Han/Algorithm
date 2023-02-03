def solution(command):
    answer = [0, 0]
    xd = [0, 1, 0, -1]
    yd = [1, 0, -1, 0]
    direction = 0
    for c in list(command):
        if c == 'R':
            direction = (direction + 1) % 4
        elif c == 'L':
            direction = (direction - 1) % 4
        elif c == 'G':
            x = answer[0] + xd[direction]
            y = answer[1] + yd[direction]
            answer = [x, y]
        else:
            x = answer[0] - xd[direction]
            y = answer[1] - yd[direction]
            answer = [x, y]

    return answer


print(solution("GRGLGRG"))
print(solution("GRGRGRB"))