# https://www.acmicpc.net/problem/2346

# 1번부터 N번까지 N개의 풍선이 원형으로 놓여져 있다 
# 1번 풍선을 터뜨리고 안에 있는 종이를 꺼내어 
# 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다 
# 양수가 적혀 있을 때는 오른쪽, 음수는 왼쪽으로 이동한다 
# 이동할 때 이미 터진 풍선은 빼고 이동한다 
# 각 풍선 안의 종이에 적혀 있는 수가 주어질 때 
# 터진 풍선의 번호를 차례로 나열한다 

from collections import deque
import sys 

n = int(input()) # 풍선의 개수
# 풍선 안에 적힌 숫자 입력 받으면서 (풍선 번호, 적힌 숫자) 튜플 형태로 저장 
balloon = deque(enumerate(map(int, input().split()), start=1))
result = [] # 결과를 저장할 리스트  

# 첫번째 풍선 터뜨리기, num 은 풍선 번호 move 은 적힌 (이동할) 숫자
num, move = balloon.popleft() 
result.append(num)

while balloon:
    # 양수이면 오른쪽으로 이동, -1은 자기 자신 제외
    if move > 0:
        balloon.rotate(-(move-1))
    # 음수면 왼쪽으로 이동 
    else:
        balloon.rotate(-move)
    
    # 다음 풍선 터뜨리기 
    num, move = balloon.popleft()
    result.append(num)

# 리스트의 원소를 공백 기준으로 펼쳐서 출력하기 
print(*result)