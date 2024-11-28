# https://www.acmicpc.net/problem/2587

# 중앙값은 주어진 수를 크기 순서대로 늘어 놓았을 때 가장 중앙에 놓은 값이다 
# 5개의 자연수의 평균과 중앙값을 구하는 프로그램을 작성하시오 

import sys

number = []
for _ in range(5): # 5개의 숫자를 한 줄씩 입력 받기 
    number.append(int(sys.stdin.readline()))

number.sort() # 정렬된 리스트에서 가운데 인덱스가 중앙값 
mid = number[(len(number)//2)] 

ave = sum(number) // len(number) # 평균값 계산 

print(ave)
print(mid)