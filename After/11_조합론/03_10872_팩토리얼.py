# https://www.acmicpc.net/problem/10872

# N! 을 출력하는 프로그램 

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    n = int(input())

    print(factorial(n))