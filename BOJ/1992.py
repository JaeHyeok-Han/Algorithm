import sys


def solution(video):
    n = len(video)
    one_count = 0
    for i in range(n):
        for j in range(n):
            if video[i][j]:
                one_count += 1
    if one_count == n * n:
        return '1'
    elif one_count == 0:
        return '0'
    else:
        sub_video_1 = video[0:n // 2]
        sub_video_2 = video[n // 2:n]
        return f'({solution([sub[0:n // 2] for sub in sub_video_1])}{solution([sub[n // 2:n] for sub in sub_video_1])}{solution([sub[0:n // 2] for sub in sub_video_2])}{solution([sub[n // 2:n] for sub in sub_video_2])})'


print(solution([list(map(int, list(sys.stdin.readline().strip()))) for _ in range(int(sys.stdin.readline()))]))
