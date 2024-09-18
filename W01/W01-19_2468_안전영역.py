# N x N 지역에서 물이 잠기지 않는 안전한 영역의
# 최대 개수를 계산하는 프로그램을 작성하시오 
# 안전 영역은 물에 잠기지 않는 지점들이 사방으로 인접해 있고
# 그 크기가 최대인 영역이다, 2 <= N <= 100 

"""
다음에
다시봐야지
"""

import sys
sys.setrecursionlimit(100000)  # 재귀 호출 깊이를 100000으로 설정하여 깊은 재귀 호출을 가능하게 함

def dfs(x, y, h):
    for m in range(4):
        nx = x + dx[m]  # 상하좌우 방향으로 이동하기 위한 x 좌표 계산
        ny = y + dy[m]  # 상하좌우 방향으로 이동하기 위한 y 좌표 계산

        if (0 <= nx < n) and (0 <= ny < n) and not visit[nx][ny] and zone[nx][ny] > h:
            # 새 위치 (nx, ny) 유효, 방문 여부 False, 물 높이가 h 보다 높은 경우
            visit[nx][ny] = True  # 새 위치를 방문한 것으로 표시
            dfs(nx, ny, h)  # 새 위치에서 재귀적으로 DFS 호출

if __name__ == '__main__':
    n = int(input())  # N x N 지역의 크기 n 입력 받기
    zone = []  # 전체 지역을 저장할 리스트
    visit = []  # 방문 여부를 저장할 리스트

    dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 x 좌표 변화량
    dy = [0, 0, -1, 1]  # 상하좌우 이동을 위한 y 좌표 변화량

    for i in range(n):
        # 각 행을 입력받아 리스트에 추가
        # 입력 받은 한 줄을 정수로 변환하여 리스트로 저장
        row = list(map(int, input().split()))  
        zone.append(row)  # row 를 zone 에 추가

    max_height = max(map(max, zone))  # zone 에서 가장 높은 물 높이 계산
    ans = 0  # 최대 안전 영역의 개수를 저장할 변수
    for k in range(max_height + 1):
        # 물 높이를 k로 설정하고, 안전 영역 계산을 반복
        visit = [[False]*n for _ in range(n)]  # 방문 여부를 나타내는 2차원 리스트 초기화
        safe = 0  # 현재 물 높이 k에서의 안전 영역 개수
        for i in range(n):
            for j in range(n):
                if zone[i][j] > k and not visit[i][j]:
                    # 현재 위치 (i, j)의 물 높이가 k보다 크고, 방문하지 않은 경우
                    safe += 1  # 안전 영역 개수 증가
                    visit[i][j] = True  # 현재 위치를 방문한 것으로 표시
                    dfs(i, j, k)  # 현재 위치에서 DFS 호출하여 안전 영역 탐색
        ans = max(ans, safe)  # 현재 물 높이에서의 안전 영역 개수와 최대값 비교

    print(ans)  # 최대 안전 영역의 개수 출력