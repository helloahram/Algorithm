import heapq

def prim(n, graph):
    mst = []  # 최소 신장 트리의 간선들을 저장할 리스트
    visited = [False] * n  # 방문 여부 확인 리스트
    min_heap = [(0, 0, -1)]  # (가중치, 현재 노드, 이전 노드)

    total_weight = 0  # 전체 가중치

    while len(mst) < n-1 and min_heap:  # 힙이 비지 않고 간선 수가 부족할 때만 반복
        weight, u, prev = heapq.heappop(min_heap)  # 가장 작은 가중치 선택
        if visited[u]:  # 이미 방문한 노드는 건너뛰기
            continue
        visited[u] = True  # 해당 노드를 방문했다고 표시
        
        if prev != -1:  # 첫 번째 노드는 이전 노드가 없으므로 추가하지 않음
            # mst.append((prev, u, weight))  # 이전 노드에서 현재 노드로의 간선 추가
            mst.append((weight, u, prev))
            total_weight += weight  # 총 가중치에 추가

        for v, w in graph[u]:  # 현재 노드와 연결된 노드들 탐색
            # v 연결된 노드 u 현재 노드 
            if not visited[v]:  # 방문하지 않은 노드만 힙에 추가 
                heapq.heappush(min_heap, (w, v, u))
                #  w 가중치 v 연결된 노드 u 현재 노드 

    if len(mst) != n-1:  # 그래프가 연결되어 있지 않은 경우
        return [], 0  # MST가 없음을 표시

    return mst, total_weight  # 간선과 전체 가중치를 반환



# 사용 예시
n = 4
graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}
mst, total_weight = prim(n, graph)  # Prim 알고리즘 실행
print("최소 신장 트리:", mst)  # 간선 출력
print("총 가중치:", total_weight)  # 전체 가중치 출력)


# while 문에서 노드를 u 로 표기하는 이유는
# 관례적으로 u 와 v 를 그래프의 노드 vertex 로 표기하기 때문
# u 는 현재 방문하고 있는 노드, v 는 이웃한 노드로 쓰인다 