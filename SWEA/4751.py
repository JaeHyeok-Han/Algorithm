def empty_line(n, flag=0):
    line = ''
    for _ in range(n):
        line += '..#.' if flag else '.#.#'
    line += '.'
    return line


def line(s):
    line = ''
    for c in s:
        line += f'#.{c}.'
    line += '#'
    return line


for _ in range(int(input())):
    string = input()
    print(empty_line(len(string), 1))
    print(empty_line(len(string)))
    print(line(string))
    print(empty_line(len(string)))
    print(empty_line(len(string), 1))
