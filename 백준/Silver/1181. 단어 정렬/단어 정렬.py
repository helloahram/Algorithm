# N 입력 받기
N = int(input())
data_list = []

# 데이터 한 줄씩 입력 받기 
for i in range(N):
    data_list.append(input().strip())

# 중복 제거 
data_list = list(set(data_list))

# 정렬
data_list.sort()
# 길이대로 정렬 
data_list.sort(key=lambda x: len(x))

# 한 줄씩 출력 
for word in data_list:
    print(word)