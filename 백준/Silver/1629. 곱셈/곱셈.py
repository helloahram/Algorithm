# https://www.acmicpc.net/problem/1629
# A 를 B 번 곱한 수를 C 로 나눈 나머지를 구하는 문제

def power(a, b, c):
    if b == 0: # 재귀 종료 조건 
        return 1
    
    # 거듭 제곱 분할 - 지수를 반으로 줄여 계산 
    half = power(a, b//2, c)
    half = (half * half) % c

    if(b % 2 != 0):
        half = (half * a) % c
    return half

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(power(a, b, c))
