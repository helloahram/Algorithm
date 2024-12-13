# https://www.acmicpc.net/problem/1764

# 듣도 못한 사람 N, 보도 못한 사람 M 이 주어질 때
# N개의 줄에 듣도 못한 사람의 이름, N+2줄부터 보도 못한 사람 이름이 주어진다 
# 듣도 보고 못한 사람의 수와 그 명단을 사전순으로 출력하는 문제 

n, m = map(int, input().split())
no_seen = set() # 듣도 못한 사람 목록 
nono = [] # 듣보잡 목록 변수 

for _ in range(n): # 듣도 못한 사람 set() 에 저장 
    no_seen.add(input().strip())

# 보도 못한 사람은 따로 저장하지 않고, 목록에 있는지 검사해서
# 목록에 있다면 result nono 에 바로 저장 
for _ in range(m): 
    name = input().strip()
    if name in no_seen:
        nono.append(name)

nono.sort() # 듣보잡 목록 정렬 

# 듣보잡 갯수 및 목록 출력 
print(len(nono))
for name in nono:
    print(name)

# 아래처럼 간단하게 만들 수도 있대 
# n, m = map(int, input().split())

# no_seen = {input().strip() for _ in range(n)} # 듣도 못한 사람 set 생성 
# # intersection() 으로 교집합을 바로 계산하여 불필요한 반복문과 리스트 조작 줄이기 
# no_heard_seen = sorted(no_seen.intersection(input().strip() for _ in range(m)))

# print(len(no_heard_seen))
# print("\n".join(no_heard_seen))