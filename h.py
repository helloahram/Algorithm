# 인덱스 A, B, C 를 각각 0, 1, 2 로 표기
graph = [[] for _ in range(3)]

# A 에서의 연결을 가중치를 포함하여 튜플로 저장
graph[0].append((1, 5))
graph[0].append((2, 2))

# B 에서 A 연결을 가중치 포함하여 튜플로 저장
graph[1]. append((0, 5))

# C 에서 A 연결을 가중치 포함하여 튜플로 저장
graph[2].append((0, 2))

print(graph)