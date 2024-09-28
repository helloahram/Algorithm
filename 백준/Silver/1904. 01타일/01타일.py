# 00 과 1 로 이루어진 타일을 붙여 
# 길이가 n 인 모든 2진 수열의 개수를
# 15746 으로 나눈 나머지를 출력하는 문제

def fibo(n):
    if n <= 1: # 기저 설정 
        return n
    list = [0] * (n+1) 
    list[0] = list[1] = 1

    # 메모이제이션 
    # for 문 안에서 나머지를 저장하여 성능 저하 방지 
    for i in range(2, n+1):
        list[i] = (list[i-1] + list[i-2]) % 15746
    # result = list[n]
    # return result
    return list[i]

if __name__ == '__main__':
    n = int(input())
    tile = fibo(n)

    print(tile)