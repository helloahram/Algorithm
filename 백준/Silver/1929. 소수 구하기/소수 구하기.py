# https://www.acmicpc.net/problem/1929
# m 이상 n 이하 소수 모두 출력하는 프로그램

import math

# 소수 판별 함수 
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

# n 과 m 사이에 소수를 구하고 출력하는 함수 
def find_all_prime(m, n):
    for i in range(m, n+1):
       if is_prime(i):
           print(i)

if __name__ == '__main__':
    m, n = map(int, input().split())
    find_all_prime(m, n)
