# https://www.acmicpc.net/problem/4948 

# n 보다 크고 2n 보다 작거나 같은 소수는 적어도 하나 존재한다 
# 자연수 n 이 주어졌을 때 n 보다 크고 2n 보다 작거나 같은 
# 소수의 개수를 구하는 프로그램을 작성하시오 
# 입력의 마지막에는 0 이 주어진다 

import sys
import math 

def eratosthenes(m):
    n = 2*m
    is_prime = [False, False] + [True] * (n+1)

    # 소수 판별  
    for i in range(2, math.isqrt(n) +1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    # 소수 개수 구하기 
    count = 0
    for i in range(m+1, n+1):
        if is_prime[i]:
            count += 1

    return count 

if __name__ == '__main__':
    result = [] # 나중에 출력할 결과를 저장할 배열 
    while(True):
        n = int(sys.stdin.readline().strip())
        if n == 0: # 입력의 마지막에는 0 이 주어진다 
            break
        # 결과를 result 에 저장하고 한 번에 출력하기 
        result.append(str(eratosthenes(n)))
    sys.stdout.write('\n'.join(result) + '\n')