# 같은 행에 있는 - 는 같은 나무 판자
# 같은 열에 있는 | 는 같은 나무 판자
# N X M 인 방에 몇 개가 필요한지 구하기

n, m = map(int, input().split()) # 바닥 크기 입력 받기

floor = [] # 바닥 패턴 
for _ in range(n):
    line = input().strip()  # 한 줄씩 입력 받기
    if len(line) != m:      # 개수가 m 이 아니면 ValueError
        raise ValueError
    floor.append(line)      # 개수가 m 이면 floor 에 추가하기 

count = 0 # 판자 개수 

# 가로 - 판자 세기 
# - 가 있으면 count++ 하고 옆에 바로 - 이면 건너뛰기 
for i in range(n): 
    j = 0 # 열 j 0 부터 m-1 까지 확인 
    while j < m: 
        if floor[i][j] == '-': # - 이 있으면 count++, j++
            count += 1
            # - 이면 count++ 없이 j++ 만 하기  
            while j < m and floor[i][j] == '-':
                j += 1
        # - 가 아니면 j++ 해서 다시 while 문 돌기 
        else:
            j += 1

# 세로 | 판자 세기 
# | 가 있으면 count++ 하고 옆에 바로 | 이면 건너뛰기 
for j in range(m): 
    i = 0 # 행 i 0 부터 n-1 까지 확인 
    while i < n: 
        if floor[i][j] == '|': # | 이 있으면 count++, i++
            count += 1
            # | 이면 count++ 없이 i++ 만 하기  
            while i < n and floor[i][j] == '|':
                i += 1
        # | 가 아니면 i++ 해서 다시 while 문 돌기 
        else:
            i += 1

print(count)