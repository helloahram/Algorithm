# https://www.acmicpc.net/problem/10870

# n 이 주어졌을 때, n 번째 피보나치 수를 구하는 프로그램


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


n = int(input().strip())
print(fibo(n))
