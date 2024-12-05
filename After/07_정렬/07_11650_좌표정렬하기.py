# https://www.acmicpc.net/problem/11650

# 2차원 평면에서 점 N개가 주어질 때, 점을 정렬하여 출력하는 문제 

# 튜플로 입력 받아서 정렬하면 되겠다 

n = int(input().strip()) # 점의 개수 
points = [] # 점들을 저장할 배열 

for i in range(n): # 입력 받기 
    x, y = map(int, input().split()) 
    points.append((x, y)) # 배열에 튜플 형태로 저장 

points.sort() # 정렬

for x, y in points: # 출력하기 
    print(x, y)
