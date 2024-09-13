# N 숫자 입력 받기
# 10의 자리 수 a 와 1의 자리 수 b 구분하기
# 10의 자리 수를 b 로, 1의 자리 수를 a + b 로 설정하기
# count+=1 해 주고 N 과 비교해서 다르면 또 돌기
# 이걸 반복해서 원래 N 과 같아지는지 확인하기 

def cycle(N, count):
    # 10 자리 수, 1자리 수 구분하기
    a = N // 10
    b = N % 10
 
    # 다시 숫자 조합하기
    # a+b 가 10보다 크다면 1자리 수만 남겨 놓기
    if a+b >= 10:
        c = (a+b) % 10
    else:
        c = (a+b)
    new = (b*10) + c
    count += 1

    # 새로운 조합과 기존 숫자가 같다면 count Return 
    if new == original:
        return count
    # 아니면 다시 재귀 돌리기 
    else:
        return cycle(new, count)

if __name__ == '__main__':
    # N 숫자 입력 받기
    original = N = int(input())

    # 사이클 길이 count 
    count = 0

    # 기존 숫자, count, 기존 
    print(cycle(N, count))