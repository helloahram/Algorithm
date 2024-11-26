# https://www.acmicpc.net/problem/1018

# N*M 보드 체스판에서 다시 칠해야 하는 정사각형의 최소값을 구하는 문제 

# 1. 체스판에서 8x8 영역 순회하여 비교
# 2. B 시작 W 시작 비교하여 최소값 선택 

n, m = map(int, input().split())

# 체스판 크기 입력 받기
board = [input().strip() for _ in range(n)]

# 체스판 패턴 정의 
pattern1 = ['WBWBWBWB', 'BWBWBWBW'] * 4 # W 시작 
pattern2 = ['BWBWBWBW', 'WBWBWBWB'] * 4 # B 시작 

min_count = float('inf') # 최소값 저장 변수 

# 8x8 체스판 모두 순회
for i in range(n-7): # 시작 행
    for j in range(m-7): # 시작 열 
        count1 = 0 # 패턴1 기준
        count2 = 0 # 패턴2 기준 

        # 8x8 부분 체스판 비교 
        for x in range(8):
            for y in range(8):
                if board[i+x][j+y] != pattern1[x][y]: # 패턴1과 비교 
                    count1 += 1 
                if board[i+x][j+y] != pattern2[x][y]: # 패턴2와 비교 
                    count2 += 1

        # 8x8 체스판 비교가 끝난 후에 최소값 갱신 
        min_count = min(min_count, count1, count2)

print(min_count)