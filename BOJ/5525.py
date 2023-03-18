import sys
import re

target = int(sys.stdin.readline()) * 2 + 1
_ = int(sys.stdin.readline())
string = sys.stdin.readline().strip()
pattern_arr = re.findall('(I(OI)+)', string)

answer = 0
for pattern in pattern_arr:
    cur_len = len(pattern[0])
    if cur_len >= target:
        answer += (len(pattern[0]) - target) // 2 + 1

print(answer)
