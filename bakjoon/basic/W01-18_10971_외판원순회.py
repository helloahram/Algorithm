# 도시 간 이동하는데 드는 비용이 행렬 W[i][j] 로 주어질 때
# 모든 도시를 모두 거쳐 다시 원래의 도시로 돌아오는
# 순회 여행 경로의 최소 비용을 구하는 프로그램을 작성하시오
# + W[i][j] 는 도시 i 에서 도시 j 로 가는 비용 

# distance_matrix 
# min_path_length 최소 비용 경로 
# visited 도시 i 의 방문 여부 

import sys

# 도시 간의 거리 정보를 Parameter 로 받는,
# 백트래킹을 하기 전에 초기화 작업을 진행하는 함수
def tsp_backtracking(distance_matrix):
    # 참고 len([row][col]) 는 row 개수
    # len([row]) 는 column 개수
    n = len(distance_matrix)
    min_path_length = sys.maxsize
    visited = [False] * n

    # current_city 현재 도시, path_length 현재까지의 경로 길이,
    # count 방문한 도시의 개수를 Parameter 로 받아서
    # 실제로 경로를 탐색하고 최단 경로를 찾는 백트래킹 재귀 함수 
    def backtrack(current_city, path_length, count):
        nonlocal min_path_length

        # 모든 도시를 방문했는지와 현재 도시에서 출발지로 돌아가는 경로가 유효한지 확인하고
        # 기존의 최소 경로와 현재까지의 경로 + 출발지로 돌아가는 경로를 비교하여 최소 경로 Update 
        if count == n and distance_matrix[current_city][0]:
            min_path_length = min(min_path_length, path_length + distance_matrix[current_city][0])
            return
        
        # 다음 방할 도시 결정하기, 현재 도시에서 갈 수 있는 모든 도시 탐색 
        for next_city in range(n):
            # next_city 의 방문 여부와 이동 가능한 거리인지 확인
            if not visited[next_city] and distance_matrix[current_city][next_city]:
                # 다음 도시의 방문 여부를 True 로 변경 (방문한 것으로 표기)
                visited[next_city] = True
                # 재귀 호출하여 다음 도시로 이동해서, 현재 경로의 길이와 방문한 도시의 개수 Update
                backtrack(next_city, path_length + distance_matrix[current_city][next_city], count + 1)
                # 재귀 호출이 완료된 후, 다음 도시의 방문 여부를 False 로 변경 (백트래킹)
                visited[next_city] = False

    # 출발 도시를 방문한 상태로 설정하고
    # 출발 도시, 초기 경로 길이, 방문한 도시 수 1 (출발 도시) 로 설정하여 백트래킹 시작 
    visited[0] = True
    backtrack(0, 0, 1)

    return min_path_length

if __name__ == '__main__':

    # 방문할 도시 N 입력 받기 
    N = int(input())
    distance_matrix = []

    for i in range(N): 
        # distance_matrix row 하나씩 입력 받기
        row = list(map(int, input().split()))
        distance_matrix.append(row)

    result = tsp_backtracking(distance_matrix)
    print(" 최단 경로 ;", result)