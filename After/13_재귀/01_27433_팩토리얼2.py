# https://www.acmicpc.net/problem/27433

# 0 보다 크거나 같은 정수 N 이 주어질 때,
# N! 을 출력하는 프로그램 (0 <= N <= 20)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input().strip())
print(factorial(n))
