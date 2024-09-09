#include <stdio.h>

# 소수 판별 에라토스테네스의 체
# 모든 수를 True 로 가정
# 제곱근까지 %2 == 0 이면 False 
def estostenes(num):
    isPrime = [True] * (num+1)

    if num < 2: isPrime[num] = False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return isPrime

# 골드바흐 파티션 만들기
# 가까운 것을 구하기 위해 n//2 부터 탐색 
def goldenbach(n, isPrime):
    for i in range(n//2, 1, -1):
        if isPrime[i] and isPrime[n-i]:
            return i, n-i

# 소수 구해놓기
isPrime = estostenes(10000)

T = int(input())
for _ in range(T):
    n = int(input())
    a, b = goldenbach(n, isPrime)
    print(a, b)