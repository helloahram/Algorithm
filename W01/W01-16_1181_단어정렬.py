# 1. 길이가 짧은 것부터
# 2. 길이가 작으면 사전 순으로
# 알파벳 소문자로 이루어진 N개의 단어 정렬 (1 <= N <= 20,000)

# 단어의 개수 N
# 입력을 받을 변수 insert
# 입력을 받을 리스트 insert_list
# 결과를 정렬할 리스트 result 

N = int(input())
# 중복 단어를 없애기 위해 set 사용 
word_list = set()

# 중복 없이 단어 추가 
for _ in range(N):
    word_list.add(input().strip())

# sorted 함수의 key 인자를 사용하여 첫 번째 기준은 단어 길이, 두 번째 기준 단어 자체
sorted_words = sorted(word_list, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)


# Merge Sort 안 해!!!!!!!
# # Merge Sort 다시 해봐야지

# def merge(a):
#     if len(a) <= 1:
#         return a
    
#     mid = len(a)//2
#     left = a[:mid]
#     right = a[mid:]

#     L = merge(left)
#     R = merge(right)

#     i = j = 0

#     while i < len(L) and j < len(R):
#         if len(L[i]) < len(R[j]) or (len(L[i]) == len(R[j]) and L[i] < R[j]):
#             if L(i) < R(j):
#                 result.append(L(i))
#                 i += 1
#             else:
#                 result.append(R(j))
#                 j += 1

# # N = int(input())
# N = 4
# a = [None] * N
# result = [None] * N

# # N 만큼 입력 받기 
# # for i in range(N):
#     # insert = input()    
# a = {'ice', 'i', 'illy', 'iii'}
# # a.append(insert)

# # 정렬하기
# insert_list = merge(a)

# # 결과 출력하기
# for i in range(N):
#     print(result)