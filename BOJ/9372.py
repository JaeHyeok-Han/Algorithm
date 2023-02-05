import sys

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    country, airplane = list(map(int, sys.stdin.readline().strip().split(" ")))
    for _ in range(airplane):
        sys.stdin.readline()
    print(country - 1)
