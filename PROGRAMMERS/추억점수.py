def solution(names, yearning, photos):
    answer = []
    dic = {}
    for i, name in enumerate(names):
        dic[name] = yearning[i]
    for photo in photos:
        temp = 0
        for people in photo:
            if people in dic:
                temp += dic[people]
        answer.append(temp)
    return answer
