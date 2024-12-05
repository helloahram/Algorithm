# https://www.acmicpc.net/problem/1181

# 알파벳 소문자로 이루어진 N개의 단어를 아래 조건에 따라 정렬하는 문제 
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로 
# 중복된 단어는 하나만 남기고 제거 

# 중복 단어는 set 으로 없애고
# 사전 순 정렬 -> 길이 순 정렬하면 되겠다 

n = int(input().strip()) # 입력 받을 단어의 개수 
word_list = [] # 입력 받은 단어를 저장할 리스트 

# 입력 받기 
for _ in range(n):
    word_list.append(input().strip())

# 중복 단어 없애기 
word_list = list(set(word_list))

# 사전 순 정렬 
word_list.sort() 
# 길이 순 정렬 
word_list.sort(key=lambda data: len(data)) 

# 단어 하나씩 출력하기 
for word in word_list:
    print(word)