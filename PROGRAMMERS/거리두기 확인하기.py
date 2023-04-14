direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def check(place):
    room = [list(line) for line in place]
    for i in range(5):
        for j in range(5):
            if room[i][j] != 'P':
                continue
            if 0 <= i + 1 < 5:
                if room[i + 1][j] == 'P':
                    return 0
                elif room[i + 1][j] == 'O':
                    if 0 <= i + 2 < 5 and room[i + 2][j] == 'P':
                        return 0
            if 0 <= i - 1 < 5:
                if room[i - 1][j] == 'P':
                    return 0
                elif room[i - 1][j] == 'O':
                    if 0 <= i - 2 < 5 and room[i - 2][j] == 'P':
                        return 0
            if 0 <= j + 1 < 5:
                if room[i][j + 1] == 'P':
                    return 0
                elif room[i][j + 1] == 'O':
                    if 0 <= j + 2 < 5 and room[i][j + 2] == 'P':
                        return 0
            if 0 <= j - 1 < 5:
                if room[i][j - 1] == 'P':
                    return 0
                elif room[i][j - 1] == 'O':
                    if 0 <= j - 2 < 5 and room[i][j - 2] == 'P':
                        return 0
            if 0 <= i + 1 < 5 and 0 <= j + 1 < 5 and room[i + 1][j + 1] == 'P':
                if room[i][j + 1] != 'X' or room[i + 1][j] != 'X':
                    return 0
            if 0 <= i - 1 < 5 and 0 <= j - 1 < 5 and room[i - 1][j - 1] == 'P':
                if room[i][j - 1] != 'X' or room[i - 1][j] != 'X':
                    return 0
            if 0 <= i + 1 < 5 and 0 <= j - 1 < 5 and room[i + 1][j - 1] == 'P':
                if room[i][j - 1] != 'X' or room[i + 1][j] != 'X':
                    return 0
            if 0 <= i - 1 < 5 and 0 <= j + 1 < 5 and room[i - 1][j + 1] == 'P':
                if room[i][j + 1] != 'X' or room[i - 1][j] != 'X':
                    return 0
    return 1

def solution(places):
    return [check(place) for place in places]