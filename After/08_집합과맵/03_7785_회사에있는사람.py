# https://www.acmicpc.net/problem/7785

# 회사 출퇴근 로그를 보고 현재 회사에 있는 사람의 이름을
# 사전 순의 역순으로 한 줄에 한 명씩 출력하는 문제 
# 알고리즘 분류 - 자료 구조, 해시를 사용한 집합과 맵 

# 사람이름 상태 로 분리해 준 다음
# Enter 이면 넣어주고, Leave 는 빼주고 
# 

n = int(input()) # 출입 기록의 수 
people = {} # 딕셔너리로 목록 관리 

for i in range(n):
    event = input().strip() # 출입 기록 입력 받기 
    name, action = event.split() # 이름과 상태로 분리 

    # 들어온 사람은 딕셔너리에 저장하고
    # 나간 사람은 딕셔너리에서 지운다 
    if action == 'enter': 
        people[name] = True # 저장 
    elif action == 'leave':
        del people[name] # 삭제 

# 딕셔너리에서 이름만 추출하고, 역순 정렬하여 출력하기 
for name in sorted(people.keys(), reverse=True):
    print(name)
