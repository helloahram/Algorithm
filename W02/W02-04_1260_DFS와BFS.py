# 아직 DFS 만 함 
def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]

    while stack:
        v = stack.pop()

        if not visited[v]:
            print(v, end=' ')
            visited[v] = True

            for neighbor in reversed(graph[v]):
                if not visited[neighbor]:
                    stack.append(neighbor)

if __name__ == '__main__':
    n, m, v = list(map(int, input().split()))
    graph = [ [] for _ in range(n+1)]

    for _ in range(m):
        u, w = map(int, input().split())
        graph[u].append(w)
        graph[w].append(u)

    dfs(graph, v)
    print('\n')