# https://www.acmicpc.net/problem/1427

# n 이 주어졌을 때, 각 자리수를 내림차순으로 정렬하는 문제 
# n <= 1,000,000,000 

# 문자열로 바꾸고 정렬해서 다시 숫자로 바꾸면 될듯? 

n = int(input().strip()) # 정렬하고자 하는 수 

num = str(n) # 입력 받은 숫자를 문자열로 변환 
sorted_num = sorted(num, reverse=True) # 내림차순 정렬 

# 정렬된 숫자를 '' 으로 join 하여 출력
print(int(''.join(sorted_num))) 
