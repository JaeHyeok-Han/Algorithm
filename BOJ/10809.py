import sys
str = sys.stdin.readline().strip()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for char in alphabet:
    if char in str:
        if char == 'z':
            print(str.index(char), end='')
        else:
            print(str.index(char), end=' ')
    else:
        print(-1, end=' ')
