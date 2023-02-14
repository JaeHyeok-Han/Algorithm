import sys
count = int(sys.stdin.readline())
numbers_list = []
numbers_dict = {}
sum_init = 0
for _ in range(count):
    num = int(sys.stdin.readline())
    numbers_list.append(num)
    if num in numbers_dict:
        numbers_dict[num] += 1
    else:
        numbers_dict[num] = 1
    sum_init += num

# 산술평균
print(round(sum_init / count))

# 중앙값
numbers_list.sort()
if count == 1:
    print(numbers_list[0])
else:
    print(numbers_list[count // 2])

# 최빈값
m = max(numbers_dict, key=numbers_dict.get)
li = [number for number in numbers_dict if numbers_dict[number] == numbers_dict[m]]
li.sort()
if len(li) == 1:
    print(li[0])
else:
    print(li[1])

# 범위
print(numbers_list[count - 1] - numbers_list[0])
