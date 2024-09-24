import heapq

def dijkstra(graph, start):
    # 거리 테이블을 무한대로 초기화하고, (노드, 거리) 형태로 저장
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    # 우선순위 큐 초기화 
    # 거리를 기준으로 정렬하기 위해 (거리, 노드) 형태로 저장 
    queue = [(0, start)]  

    while queue:
    	# heapq.heappop() 로 queue 에서 제일 짧은 거리를 가진 노드를 꺼낸다 
        current_distance, current_node = heapq.heappop(queue)

        # 현재 처리 중인 노드의 거리가 기록된 거리보다 크다면 
        # 이미 최적의 경로로 처리되었으므로 무시한다 
        # current_distance 는 우선순위 큐에서 꺼낸 값
        # dist[current_node] 현재 노드까지의 최단 거리
        if current_distance > dist[current_node]:
            continue

		# for 문으로 인접 노드와 가중치 차례로 확인 
        for next_cost, next_node in graph[current_node].items():
            new_distance = current_distance + next_node

            # 더 짧은 경로가 발견되면 거리 테이블을 갱신하고 우선순위 큐에 추가
            if dist[next_cost] > new_distance:
                dist[next_cost] = new_distance
                heapq.heappush(queue, (new_distance, next_cost))

    return dist

if __name__ == '__main__':
    # N 도시의 개수 M 도로의 개수 K 거리 정보 X 출발 도시의 번호 
    N, M, K, X = map(int, input().split())
    
    # K = int(input())

    # graph = {
    #     '1' : {'2': 1, '3': 1},
    #     '2' : {'3': 1, '4': 1},
    #     '3' : {},
    #     '4' : {}
    # }

    graph = {i: {} for i in range(1, N+1)}
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u][v] = 1

    node_result = []
    result = dijkstra(graph, X)
    for node, edge in result.items():
        if edge == K:
            node_result.append(str(node))
    
    if not node_result:
        print(-1)
    else:
        print(" ".join(node_result))