# https://www.acmicpc.net/problem/17103 

# 골드바흐의 추측 - 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다 
# 짝수 n 을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다 
# 짝수 n 이 주어졌을 때, 골드바흐 파티션의 개수를 출력하는 프로그램 

import math
import sys 

# 에라토스테네스로 소수 구하기 
def eratosthenes(n):
    is_prime = [False, False] + [True] * (n+1)

    for i in range(2, math.isqrt(n)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return is_prime

# 골든바흐 파티션 구하기 
def goldenbach(n):
    is_prime = eratosthenes(n)
    count = 0

    # i 과 n-i 이 중복되지 않게 n//2 까지만  
    for i in range(2, n//2 + 1):
        if is_prime[i] and is_prime[n-i]:
            count += 1

    return count

if __name__ == '__main__':
    t = int(input()) # Test Case 개수 
    result = []

    for _ in range(t):
        n = int(input()) 
        result.append(str(goldenbach(n)))
    sys.stdout.write('\n'.join(result)+'\n')