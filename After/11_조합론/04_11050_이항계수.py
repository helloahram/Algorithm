# https://www.acmicpc.net/problem/11050

# 자연수 N 과 정수 K 가 주어졌을 때
# 이항 계수 (N K)를 구하는 프로그램 

# 이항 계수는 n!/k!(n-k)! 라고 한다 

def factorial(i):
    if i == 0: return 1
    return i * factorial(i-1)

n, k = map(int, input().split())

result = factorial(n) // (factorial(k) * factorial(n-k))
print(result)