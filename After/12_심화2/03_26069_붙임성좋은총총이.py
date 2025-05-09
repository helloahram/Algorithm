# https://www.acmicpc.net/problem/26069

# N번을 걸쳐 사람을 만난다 
# ChongChong 을 만난 사람은 무지개 댄스를 추게 된다 
# 마지막에 무지개 댄스를 추는 사람을 구하는 문제 

n = int(input()) # 사람들이 만난 기록의 수 
dance_set = {'ChongChong'} # 춤추는 사람 집합 

for _ in range(n):
    a, b = input().split() # 만난 사람 이름 받기 
    # a 또는 b 가 dance_set 에 존재하면 둘 다 추가 
    if a in dance_set or b in dance_set:
        dance_set.add(a)
        dance_set.add(b)

# 집합의 길이 출력 
print(len(dance_set)) 