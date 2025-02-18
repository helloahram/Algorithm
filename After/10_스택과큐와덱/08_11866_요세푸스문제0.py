# https://www.acmicpc.net/problem/11866

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아 있고
# 순서대로 k번째 사람을 제거한다 

# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다 
# N과 K가 주어질 때 (N, K)-요세푸스 순열을 구하는 프로그램 

# deque.rotate 로 k-1 을 맨 앞으로 옮기고 
# popleft 로 제거해서 반복하기

from collections import deque

n, k = map(int, input().split())
# 1부터 n까지 deque 에 삽입하기 
queue = deque(range(1, n+1))

result = [] # 요세푸스 순열 저장

while queue:
    # (k-1) 번째 사람이 맨 앞으로 오도록 회전 
    queue.rotate(-(k-1))
    # 맨 앞인 k번째 사람 제거 후 결과에 추가 
    result.append(queue.popleft())

print(f"<{', '.join(map(str, result))}>")