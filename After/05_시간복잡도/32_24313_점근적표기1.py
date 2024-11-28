# https://www.acmicpc.net/problem/24313

# 빅오 표기법은 다음과 같이 정의할 수 있다 
# O(g(n)) = {f(n) | 모든 n ≥ n0 에 대하여 f(n) ≤ c × g(n)인 
# 양의 상수 c와 n0가 존재한다}

# 함수 f(n) = a1n + a0, 양의 정수 c, n0 가 주어질 경우
# O(n) 정의를 만족하면 1, 아니면 0 을 출력하는 문제 

# 간단하게 a1n + a0 <= c * n 검사만 하면 되겠다

import sys

def check_condition(n, a1, a0, c):
    return (a1 * n + a0) <= (c * n)

try:
    a1, a0 = map(int, input().split())
    c = int(input())
    n0 = int(input())

    # n0 부터 시작해서 조건을 만족하는 n 이 있는지 확인 
    result = 1
    for n in range(n0, 101):
        if not check_condition(n, a1, a0, c):
            result = 0
            break

    print(result)

except EOFError:
    # 입력이 끝나면 프로그램 종료 
    sys.exit()
except ValueError as e:
    # 잘못된 입력 형식인 경우 에러 메시지 출력
    print(f"입력 오류 {e}")
    sys.exit()

# 프로그램 종료 
exit()














# 입력 받기 
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input)

#  f(n) 과 c * n 검사하는 함수 
def check_condition(n): 
    return a1 * n + a0 <= c * n

# n01 부터 조건 만족 여부 확인
result = 1
for n in range(n0, n0+1000):
    if not check_condition(n):
        result = 0
        break

print(result)