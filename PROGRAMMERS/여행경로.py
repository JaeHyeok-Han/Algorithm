def solution(tickets):
    temp = []
    tickets_obj = {}
    count = {}
    visited = {}
    for ticket in tickets:
        temp += ticket
    temp = list(set(temp))
    for t in temp:
        tickets_obj[t] = []
    for start, end in tickets:
        tickets_obj[start].append(end)
        if start + end in count:
            count[start + end] += 1
        else:
            count[start + end] = 1
        if start + end not in visited:
            visited[start + end] = 0
    for start in tickets_obj:
        tickets_obj[start].sort()

    def dfs(town, path):
        if len(path) == len(tickets) + 1:
            return path
        for n in tickets_obj[town]:
            if visited[town + n] < count[town + n]:
                path.append(n)
                visited[town + n] += 1
                temp = dfs(n, path)
                if len(temp) == len(tickets) + 1:
                    return temp
                else:
                    path.pop()
                    visited[town + n] -= 1
        return path

    return dfs('ICN', ['ICN'])
