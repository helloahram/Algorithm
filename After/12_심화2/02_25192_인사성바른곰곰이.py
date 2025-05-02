# https://www.acmicpc.net/problem/25192

# 새로운 사람이 채팅방에 입장한 이후 처음 채팅을 입력하는 사람은 
# 곰곰티콘으로 인사를 한다, 채팅 기록 중 곰곰티콘이 사용된 횟수 

# 채팅방의 기록 수 
n = int(input()) 

users = set() # 중복 방지 유저 목록 
result = 0 # 곰곰티콘 사용 횟수 

# ENTER 이후 users 를 Set 으로 중복 확인
# 그 이후 ENTER 가 나오면 users Reset 

for _ in range(n):
    line = input().strip()

    # 새로운 유저 입장 시 유저 목록 초기화 
    if line == 'ENTER':
        users.clear() 
    # 새로운 유저 입장 후 처음 채팅하는 경우
    # 유저 목록에 추가 및 결과 +1 
    else:
        if line not in users:
            users.add(line)
            result += 1
        
print(result)
