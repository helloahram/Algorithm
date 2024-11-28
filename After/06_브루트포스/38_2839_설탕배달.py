# https://www.acmicpc.net/problem/2839

# 3키로와 5키로 봉지로 N키로의 설탕을 배달할 때 
# 최소한의 봉지 개수를 구하는 문제 
# 정확하게 N키로를 만들 수 없다면 -1 출력 

n = int(input()) # 설탕 N키로 
box = 0 # 봉지 개수 

while n >= 0: # 5키로 봉지에 담기 
    # 5로 나누어 떨어지면 5로 나눈 몫 출력 
    if n % 5 == 0:
        box += n // 5
        print(box)
        break
    # 5 로 나누어 떨어지지 않으면 3키로 먼저 사용 
    n -= 3 
    box += 1
# 정확히 나눌 수 없으면 -1 출력 
else:
    print(-1)

