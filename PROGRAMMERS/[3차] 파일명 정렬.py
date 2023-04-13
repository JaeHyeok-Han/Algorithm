def convert(string):
    result = []
    mode = 0
    temp = ''
    for s in string:
        if mode == 0:
            if s.isdigit():
                r = ''
                for t in temp:
                    if t not in [' ', '.', '-']:
                        r += t.upper()
                    else:
                        r += t
                result.append(r)
                temp = s
                mode = 1
            else:
                temp += s
        elif mode == 1:
            if s.isdigit():
                temp += s
            else:
                break
    result.append(int(temp))
    return result


def solution(files):
    files.sort(key=lambda x: (convert(x)[0], convert(x)[1]))
    return files
