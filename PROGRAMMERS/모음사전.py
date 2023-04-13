def solution(word):
    dic = {'A': '1', 'E': '2', 'I': '3', 'O': '4', 'U': '5'}
    count = [781, 156, 31, 6, 1]
    string = ''
    for w in word:
        string += dic[w]
    while len(string) < 5:
        string += '0'
    answer = 0
    for i, w in enumerate(string):
        if w == '0':
            break
        answer += (int(w) - 1) * count[i]
        answer += 1

    return answer
