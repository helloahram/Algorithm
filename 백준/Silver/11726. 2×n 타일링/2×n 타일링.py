# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 
# 10,007 로 나눈 나머지를 출력한다 
# 1 <=n <= 1,000

def rect(n):
    list = [0] * (n+1) # 결과 정리 
    if n <= 1: # 기저 설정
        return n
    list[1] = 1
    list[2] = 2
    
    for i in range(3, n+1):
        list[i] = (list[i-1] + list[i-2]) % 10007
        
    result = list[n]

    return result 

if __name__ == '__main__':
    n = int(input())
    print(rect(n))