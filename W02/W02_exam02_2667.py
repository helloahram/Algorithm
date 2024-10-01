# N X N 인 정사각형 마을 안에 1 이 상하좌우로 연결되어 있으면 같은집
# 같은집의 단지 수, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력 

def dfs(x, y):
    # 0 < x, y <= n 의 조건을 만족하지 않거나, 0 이면 넘어가기 
    if x < 0 or x >= n or y < 0 or y >= n or map[x][y] == 0:
        return 0
    
    map[x][y] = 0
    count = 1

    

if __name__ == '__main__':
    n = int(input())
    map = []

    for _ in range(n):
        line = input().strip()  # 한 줄씩 입력 받기
        if len(line) != n:      # 개수가 n 이 아니면 ValueError
            raise ValueError
        map.append(line)        # 개수가 n 이면 map 에 추가하기 

    total_count = 0 
    

    