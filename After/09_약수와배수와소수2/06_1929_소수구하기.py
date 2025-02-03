# https://www.acmicpc.net/problem/1929
# m 이상 n 이하 소수 모두 출력하는 프로그램

import math
import sys 

def eratosthenes(m, n):
    # 0, 1 은 소수 아님 
    is_prime = [False, False] + [True] * (n-1)

    # 소수 판별 
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    # m 이상 n 이하 소수 출력 
    for i in range(m, n+1):
        if is_prime[i]:
            sys.stdout.write(str(i)+ '\n')

if __name__ == '__main__':
    m, n = map(int, input().split())
    eratosthenes(m, n)

# 원래 작성했던 코드 
# import math

# # 소수 판별 함수 
# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True

# # n 과 m 사이에 소수를 구하고 출력하는 함수 
# def find_all_prime(m, n):
#     for i in range(m, n+1):
#        if is_prime(i):
#            print(i)

# if __name__ == '__main__':
#     m, n = map(int, input().split())
#     find_all_prime(m, n)
