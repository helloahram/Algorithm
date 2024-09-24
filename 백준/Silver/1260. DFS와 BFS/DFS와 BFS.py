from collections import deque

def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]

    while stack:
        v = stack.pop()

        if not visited[v]:
            print(v, end=' ')
            visited[v] = True

            for neighbor in sorted(graph[v], reverse=True):
                if not visited[neighbor]:
                    stack.append(neighbor)

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])

    while queue:
        v = queue.popleft()

        if not visited[v]:
            print(v, end=' ')
            visited[v] = True

            for neighbor in sorted(graph[v]):
                if not visited[neighbor]:
                    queue.append(neighbor)

if __name__ == '__main__':
    n, m, v = list(map(int, input().split()))
    graph = [ [] for _ in range(n+1)]

    for _ in range(m):
        # 입력으로 주어지는 간선은 양방향이다 
        u, w = map(int, input().split())
        graph[u].append(w)
        graph[w].append(u)

    dfs(graph, v)
    print() # 줄바꿈
    bfs(graph, v)
    print() # 줄바꿈