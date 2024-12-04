# https://www.acmicpc.net/problem/10814

# 회원들을 나이가 증가하는 순으로,
# 나이가 같으면 먼저 가입한 사람 순으로 정렬하는 문제 
# 1<= 나이 <= 200, 입력한 순서가 가입한 순서

# 입력 받을 때는 str 로 받고 나이 형변환
# 나이 순으로 정렬한 다음
# 나이가 같으면 i 가 빠른 순으로 정렬 

n = int(input())
members = []

# 입력 받기 
for i in range(n):
    age, name = input().split()
    age = int(age) # 나이는 숫자로 형변환 
    members.append((age, name, i)) # i 가입 순서 

# 1 나이 2 가입 순서 순으로 정렬
members.sort(key=lambda data: (data[0], data[2])) 

# 차례로 출력 
for age, name, _ in members:
    print(age, name)