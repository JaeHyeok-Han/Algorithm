import sys
from itertools import product

target = int(sys.stdin.readline())
if target == 100:
    print(0)
else:
    wrong_count = int(sys.stdin.readline())
    answer = abs(target - 100)
    if not wrong_count:
        print(min(answer, len(str(target))))
    else:
        wrong_btn = list(map(int, sys.stdin.readline().strip().split(' ')))
        btn = [str(i) for i in range(10) if i not in wrong_btn]

        def convert(string):
            if string:
                s = ''.join(string)
                return int(s)
            else:
                return answer

        if not len(btn):
            print(answer)
        else:
            temp1 = list(map(convert, list(product(btn, repeat=len(str(target))))))
            temp2 = list(map(convert, list(product(btn, repeat=(len(str(target))) + 1))))
            if len(str(target)) > 1:
                temp3 = list(map(convert, list(product(btn, repeat=(len(str(target))) - 1))))
                temp = list(set(temp1 + temp2 + temp3))
            else:
                temp = list(set(temp1 + temp2))
            for number in temp:
                new_answer = abs(target - number) + len(str(number))
                if new_answer < answer:
                    answer = new_answer

            print(answer)
