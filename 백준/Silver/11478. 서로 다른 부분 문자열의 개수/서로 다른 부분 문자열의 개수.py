# https://www.acmicpc.net/problem/11478

# 주어진 문자열에서 서로 다른 부분 문자열의 개수를 구하는 문제 
# 

str = input().strip() # 문자열 입력 받기 
sub_strings = set() # 부분 문자열을 저장할 set - 중복 방지

# 첫번째 글자부터 한 글자씩 추가하여 부분 문자열 만들기 
for i in range(len(str)):
    # 현재 인덱스부터 끝까지의 모든 부분 문자열 탐색 
    for j in range(i+1, len(str)+1):
        sub_strings.add(str[i:j])

# 부분 문자열의 개수 출력
print(len(sub_strings))