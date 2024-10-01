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
