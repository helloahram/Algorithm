from collections import deque

# 위상 정렬 함수
def topological_sort(n, graph):
    # 모든 노드의 진입 차수 초기화
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1

    # 진입 차수가 0인 노드들을 큐에 삽입
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    
    # 위상 정렬 결과 리스트
    topo_order = []

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드를 하나 꺼내서 결과에 추가
        node = queue.popleft()
        topo_order.append(node)

        # 해당 노드와 연결된 모든 노드들의 진입 차수를 1씩 감소
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # 진입 차수가 0이 되면 큐에 삽입
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 모든 노드를 방문하지 못하면 사이클이 존재하는 것
    if len(topo_order) != n:
        return None  # 사이클이 존재하는 경우

    return topo_order  # 위상 정렬 결과 반환

# 테스트용 그래프 (노드 0부터 시작)
n = 6  # 노드 수
graph = {
    0: [2, 3],  # 0번 노드에서 2, 3번 노드로
    1: [3, 4],  # 1번 노드에서 3, 4번 노드로
    2: [3],     # 2번 노드에서 3번 노드로
    3: [5],     # 3번 노드에서 5번 노드로
    4: [5],     # 4번 노드에서 5번 노드로
    5: []       # 5번 노드는 끝점
}

# # 사용자로부터 그래프 입력 받기
# def input_graph():
#     n = int(input("노드의 개수를 입력하세요: "))
#     graph = {}

#     for i in range(n):
#         edges = input(f"{i}번 노드에서 연결된 노드를 공백으로 구분하여 입력하세요 (없으면 그냥 엔터): ").strip()
#         if edges:
#             graph[i] = list(map(int, edges.split()))
#         else:
#             graph[i] = []
    
#     return n, graph

# n, graph = input_graph()

result = topological_sort(n, graph)
if result:
    print("위상 정렬 결과:", result)
else:
    print("사이클이 존재합니다.") 
