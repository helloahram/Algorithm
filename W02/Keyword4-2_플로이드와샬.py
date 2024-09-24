# 무한대를 나타내기 위한 값 설정 
INF = float('inf')

def floyd_warshall(n, graph):
    # 각 노드에서 다른 노드로 가는 최소 거리를 기록할 배열 
    # 초기값은 무한대로 설정  
    dist = [[INF]*n for _ in range(n)]

    # 자기 자신으로 가는 거리는 0 으로 설정 
    for i in range(n):
        dist[i][i] = 0

    # 주어진 그래프의 거리 정보를 거리 dist 배열에 초기화 
    for u in range(n):
        for v in range(n):
            dist[u][v] = graph[u][v]

    # 플로이드 와샬 알고리즘 적용
    # k 는 거쳐가는 노드, i 는 출발 노드, j 는 도착 노드 
    for k in range(n):
        for j in range(n):
            for i in range(n):
                # 기존 dist[i][j] 의 값과 dist[i][k] + dist[k][j] 의 값을 비교 
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    return dist

if __name__ == '__main__':

    # 입력 예시 
    n = 4 # 노드의 개수 
    graph = [
        [0, 4, INF, 6],
        [3, 0, 7, INF],
        [5, INF, 0, 4],
        [INF, INF, 2, 0]
    ]

    # 플로이드 와샬 알고리즘 수행 
    result = floyd_warshall(n, graph)

    # 결과를 2차원 배열 형태로 출력 
    for row in result:
        print(row)
    