from collections import deque
import sys

n = int(sys.stdin.readline().strip())  # 자료구조의 개수
a = list(map(int, sys.stdin.readline().split()))  # 0은 큐, 1은 스택
b = list(map(int, sys.stdin.readline().split()))  # 초기 값들
m = int(sys.stdin.readline().strip())  # 삽입할 수열의 길이
c = list(map(int, sys.stdin.readline().split()))  # 삽입할 원소들

structures = []
result = []
queue = deque()

for i in range(n):
    if a[i] == 0:
        structures.append(deque([b[i]]))
    else:
        structures.append([b[i]])

for value in c:
    x = value
    for i in range(n):
        if a[i] == 0:
            structures[i].append(x)
            x = structures[i].popleft()
        else:
            structures[i].append(x)
            x = structures[i].pop()
    result.append(x)

print(*result)