# https://www.acmicpc.net/problem/1436

# 666 다음은 1666, 2666, 3666 순서로 영화 제목을 지을 때
# N번째 영화의 제목이 들어간 수를 출력하는 프로그램

# N 은 연속된 666 을 포함한 N번째 숫자이다 
# 666 이 들어간 숫자를 카운팅하면 되겠다 

n = int(input()) # n번째 영화의 제목 
count = 0
i = 666 # 시작 숫자 

while count < n:
    if '666' in str(i): # 666 포함 여부 확인 
        count += 1 
    i += 1 # 다음 숫자 확인 

print(i - 1) # n번째 숫자 출력 

# 처음 작성한 코드 
# # n번째 666을 완전 탐색하기 
# for i in range(666, 9999999):
#     # str(i) 에 666 이 있으면 
#     # title 에 str(i) 을 저장하고 count++
#     if '666' in str(i):
#         title = str(i)
#         count += 1

#         # n 이 count 와 같으면 title 출력하고 끝 
#         if n == count:
#             print(title)
#             break
