# https://www.acmicpc.net/problem/4134

# 정수 n이 주어졌을 때, n보다 크거나 같은 소수 중 
# 가장 작은 소수를 찾는 프로그램을 작성하시오 

import sys
import math

# 소수 구하기 
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# n보다 크거나 같은 가장 작은 소수 찾기 
def find_next_prime(n):
    while not is_prime(n):
        n += 1
    return n

result = [] # 결과 저장 

t = int(input())
for i in range(t):
    n = int(sys.stdin.readline().strip())
    result.append(str(find_next_prime(n)))

# join 으로 한꺼번에 출력 
sys.stdout.write("\n".join(result)+"\n")