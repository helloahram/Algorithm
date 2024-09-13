# 정수 N 으로 N! 출력하는 프로그램 작성하기

# 정수 N 입력 받기 ( 0 <= N <= 12 )

# 1부터 N 까지 자기 자신에게 곱해주기
# 일반 함수로
# def factorial(N):
#     # Total 초기값 1 로 설정 
#     # N 도 곱해줘야 하니 N+1 까지 
#     total = 1
#     for i in range(1, N+1):
#         total *= i
#     return total

# num = int(input())
# print(factorial(num))

def factorial2(N):
    if N == 0: return 1
    return (N * factorial2(N-1))

num = int(input())
print(factorial2(num))
