def dfs(graph, start):
    # 방문 여부를 기록하는 리스트
    visited = [False] * len(graph)
    # 스택 초기화 (시작 노드 넣기)
    stack = [start]

    while stack:
        # 스택에서 노드를 꺼냄
        v = stack.pop()

        # 방문하지 않았다면 방문 처리
        if not visited[v]:
            print(v, end=' ')  # 방문한 노드 출력
            visited[v] = True

            # 연결된 노드를 스택에 추가 (역순으로 넣어야 DFS 순서와 일치)
            for neighbor in reversed(graph[v]):
                if not visited[neighbor]:
                    stack.append(neighbor)

# 예시 그래프 (인접 리스트로 표현)
graph = [
    [],           # 0번 노드는 사용하지 않음 (노드 번호를 1부터 시작하기 위해)
    [2, 3, 8],    # 1번 노드와 연결된 노드들
    [1, 7],       # 2번 노드와 연결된 노드들
    [1, 4, 5],    # 3번 노드와 연결된 노드들
    [3, 5],       # 4번 노드와 연결된 노드들
    [3, 4],       # 5번 노드와 연결된 노드들
    [7],          # 6번 노드와 연결된 노드들
    [2, 6, 8],    # 7번 노드와 연결된 노드들
    [1, 7]        # 8번 노드와 연결된 노드들
]

# DFS 비재귀적 호출
dfs(graph, 1)