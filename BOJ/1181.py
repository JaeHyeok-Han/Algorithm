import sys
word_count = int(sys.stdin.readline())
words = []
for _ in range(word_count):
    words.append(sys.stdin.readline().strip())
words = list(set(words))
words.sort(key=lambda x: (len(x), x))
for word in words:
    print(word)
