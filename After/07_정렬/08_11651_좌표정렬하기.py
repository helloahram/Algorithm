# https://www.acmicpc.net/problem/11651

# 2차원 평면 위의 점 N개를 y좌표 오름차순 기준으로 정렬하는 문제 

n = int(input().strip())
points = [] # 입력된 좌표를 저장할 리스트 

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y)) # 튜플 형태로 저장 

# y 기준으로 오름차순 정렬, y 가 같으면 x 기준 정렬 
points.sort(key=lambda point: (point[1], point[0])) 

# 정렬된 좌표 출력 
for x, y in points: 
    print(x, y)