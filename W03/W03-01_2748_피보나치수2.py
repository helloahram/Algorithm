# 피보나치 f(0) = 1, f(1) = 1, f(n) = f(n-1)+f(n-2)

def fibo(n):
    if n <= 1: # 기저 설정 
        return n 
    
    list = [0] * (n+1) # 결과 리스트 선언 및 초기화 
    list[1] = 1 # 피보나치 수열에서 첫번째 값은 1

    # 메모이제이션으로 피보나치 함수 구현 
    for i in range(2, n+1): # 2부터 n까지 반복
        # fibo[n] = fibo[n-1] + fibo[n-2]
        list[i] = list[i-1] + list[i-2]
    result = list[n] # 마지막 계산 결과를 result 에 저장 

    return result

if __name__ == '__main__':
    n = int(input()) # n 입력 받기 

    print(fibo(n)) # 결과값 출력 


# # 피보나치 수열을 하향식으로 계산하는 함수 (재귀+메모이제이션)
# def fibonacci(n, result):
#     if n in result: # 이미 계산된 값이 있다면 그 값을 반환
#         return result[n]
#     if n <= 1: # 기저 사례, n == 0 or 1
#         return n
#     result[n] = fibonacci(n-1, result) + fibonacci(n-2, result)
#     return result[n]

# if __name__ == '__main__':
#     n = int(input()) 
#     print(fibonacci(n, {}))

# 피보나치 수열을 상향식으로 계산하는 함수 (반복문 + 테이블)
# def fibo_bottom_up(n):
#     if n <= 1: # 기저 사례, n == 0 or 1
#         return n
#     result = [0] * (n+1) # 결과 테이블 
#     result[1] = 1 # 초기값 설정 
    
#     for i in range(2, n+1):
#         result[i] = result[i-1] + result[i-2] # 이전 두 값 합산 
#     return result[n]  # n번째 피보나치 값 반환

# if __name__ == '__main__':
#     n = int(input())
#     print(fibo_bottom_up(n))