# Algorithm
백준, SW Expert Academy, 프로그래머스에서 푼 문제들을 기록하는 레포지토리입니다.

# 파이썬 꿀팁
```python
# 삼항연산자 (뒤에 연달아 붙이는거 됨)
trueValue if 조건문 else falseValu

# 몫 구하기
num1 // num2

# 몫, 나머지 한 번에 구하기 (리스트로 반환됨)
divmod(num1, num2)

# 정수로 변환
int(2.5)  # 2, 내림으로 반환됨
int(11, 2)  # 3, 두 번째 인자를 주면 해당 진수로 해석

# 문자열로 변환
str(123)  # '123'

# range()
range(5)  # 0, 1, 2, 3, 4
range(2, 5)  # 2, 3, 4
range(0, 10, 2)  # 2, 4, 6, 8

# 리스트 순회
for ele in 리스트

# 리스트 길이 반환
len(리스트)

# 리스트 뒤집기 (문자열도 됨)
리스트[::-1]

# 파이썬의 &&, ||
&&는 and, ||는 or

# 파이썬에서 ++, -- 안 됨

# 리스트의 모든 요소에 대해 같은 함수 적용한 값으로 이루어진 리스트
list(map(함수, 리스트))

# 리스트의 모든 요소에 대해 같은 함수를 적용해 반환값이 true인 값으로 이루어진 리스트
list(filter(함수, 리스트))

# 리스트에서 어떤 요소의 개수 구하기
리스트.count(요소)

# 리스트에서 어떤 요소를 다른 요소로 바꾸기
리스트.replace(타켓, 요소)

# 파이썬에서 간단한 함수를 만들때는 lamda 사용
list(map(lamda x: x * 2, 리스트))

# 리스트 정렬
리스트.sort()  # 오름차순
리스트.sort(reverse=True)  # 내림차순
리스트.sort(key= lambda x: 원하는 정렬조건이 순서대로 담긴 튜플)

# 리스트를 set으로 바꾸기
set(리스트)

# set간의 중복요소 리스트 구하기
list(set1 & set2)

# 리스트 포함 여부
if 요소 in 리스트

# 제곱수와 제곱근 구하기
import math
math.pow(num1, num2)  # 제곱수
math.sqrt(num1)  # 제곱근
num ** 0/5  # 제곱근

# 숫자 판별
요소.isdigit()

# 무시해야 되는 경우
pass

# 거듭 제곱 (사칙연산보다 우선순위가 높으므로 주의)
**

# 대문자, 소문자로 변환
요소.upper()
요소.lower()

# 대문자, 소문자 검사
요소.isupper()
요소.islower()

# 대문자는 소문자로, 소문자는 대문자로 변환
문자열.swapcase()

# 숫자 변환
num1, num2 = num2, num1

# 리스트 최대값, 최소값
max(리스트)
min(리스트)

# 리스트에서 특정값의 인덱스
리스트.index(요소)

# 리스트 문자열로 합치기
''.join(리스트)

# for문과 if문 같이쓰기
[i for i in 리스트 if 조건문]

# 깊은 복사
from copy import deepcopy
deepcopy(리스트)

# deque
from collections import deque
deq = deque()
deq.appendleft()  # 시작점에 추가
deq.append()  # 끝점에 추가
deq.popleft()  # 시작점에서 삭제
deq.pop()  # 끝점에서 삭제

# 함수안에서 함수밖의 변수를 제어하고 싶을때 사용하는 키워드
def outter:
    a = 10
    def inner:
        nonlocal a
        a += 10

# 최대 재귀 깊이 수정 (백준에서는 기본적으로 1000으로 설정되어 있음)
import sys
sys.setrecursionlimit(깊이)

# 순열, 조합
```