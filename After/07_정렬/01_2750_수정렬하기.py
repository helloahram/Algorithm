# https://www.acmicpc.net/problem/2750

# N개의 수를 오름차순으로 정렬하는 프로그램 
# 수의 개수와 수를 입력 받는다
# 제한 시간 1초, 메모리 128MB

n = int(input())
# number = list(map(int, input().split())) # 한 줄로 입력 받기
number = [int(input()) for i in range(n)] # 여러 줄로 입력 받기 

number.sort() # sort() 는 반환값이 없다 
# number = sorted(number) # sorted 는 정렬된 리스트를 반환한다 

for i in range(n):
    print(number[i])