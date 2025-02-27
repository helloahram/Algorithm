def factorial2(N):
    if N == 0: return 1
    return (N * factorial2(N-1))

num = int(input())
print(factorial2(num))