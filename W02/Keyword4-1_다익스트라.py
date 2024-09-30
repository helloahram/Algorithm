import heapq

def dijkstra(graph, start, N):
    # 거리 테이블을 무한대로 초기화하고, (노드, 거리) 형태로 저장
    dist = [float('inf')] * N
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
        for next_node, next_cost in graph[current_node]:
            new_distance = current_distance + next_cost

            # 더 짧은 경로가 발견되면 거리 테이블을 갱신하고 우선순위 큐에 추가
            if dist[next_node] > new_distance:
                dist[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))

    return dist

if __name__ == '__main__':
    
    # 그래프 예시 (인접 리스트)
    N = 4
    graph = [
        [(1, 1), (2, 4)],  # A -> B(1), A -> C(4)
        [(0, 1), (2, 2), (3, 5)],  # B -> A(1), B -> C(2), B -> D(5)
        [(0, 4), (1, 2), (3, 1)],  # C -> A(4), C -> B(2), C -> D(1)
        [(1, 5), (2, 1)]  # D -> B(5), D -> C(1)
    ]

    # 문자열 노드 A B C D 를 인덱스와 매핑
    node_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    reversed_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

    start = 'A' # 시작 노드 
    start_node = node_map[start]
    
    print(dijkstra(graph, start_node, N))
    # 결과 출력
    # [0, 1, 3, 4]