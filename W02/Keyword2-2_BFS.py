from collections import deque

def bfs(graph, start):
    # 방문 여부를 기록하는 리스트 
    # 각 노드에 대해 방문했는지 여부를 표시 
    visited = [False] * len(graph)
    # 큐 초기화 (시작 노드 넣기)
    # deque 를 생성하기 위해 인자로 리스트를 전달 
    queue = deque([start])

    while queue:
        # 큐에서 노드를 꺼냄
        v = queue.popleft()

        # 방문하지 않았다면 방문 처리
        if not visited[v]:
            print(v, end=' ')   # 방문하지 않았다면 방문 처리
            visited[v] = True   # 방문한 노드 표시 

            # 연결된 노드를 큐에 추가 
            for neighbor in graph[v]:
                if not visited[neighbor]: # 아직 방문하지 않은 이웃 노드
                    queue.append(neighbor) # 이웃 노드를 큐에 추가 

if __name__ == '__main__':
    # 예시 그래프 (인접 리스트로 표현)
    graph = [
        [],          # 0번 노드는 사용하지 않음 (노드 번호를 1부터 시작하기 위해)
        [2, 3],      # 1번 노드와 연결된 노드들
        [4, 5],      # 2번 노드와 연결된 노드들
        [1, 6],      # 3번 노드와 연결된 노드들
        [2],         # 4번 노드와 연결된 노드들
        [2],         # 5번 노드와 연결된 노드들
        [3],         # 6번 노드와 연결된 노드들
    ]

    # BFS 비재귀적 호출
    bfs(graph, 1)
    # 줄바꿈
    print()

    # 결과 출력
    # 1 2 3 4 5 6