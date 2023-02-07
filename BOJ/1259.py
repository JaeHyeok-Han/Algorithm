import sys
while True:
    str = sys.stdin.readline().strip()
    if str == '0':
        break
    else:
        if str == str[::-1]:
            print('yes')
        else:
            print('no')
