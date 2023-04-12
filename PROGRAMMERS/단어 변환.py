from collections import deque


def dif_count(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return True if count == 1 else False


def solution(begin, target, words):
    queue = deque()
    queue.append(begin)
    visited = {}
    visited[begin] = 0
    flag = False
    while queue:
        cur = queue.popleft()
        if cur == target:
            flag = True
            break
        for word in words:
            if word not in visited and dif_count(cur, word):
                queue.append(word)
                visited[word] = visited[cur] + 1

    if flag:
        return visited[target]
    else:
        return 0
