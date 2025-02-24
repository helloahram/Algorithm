# https://www.acmicpc.net/problem/24511

# 시간 제한 1초, 추가 시간 없대 

# x0 을 입력 받고 1번 자료 구조에 삽입한 뒤
# 1번 자료 구조에서 원소 x1 를 pop 한다 
# x1 를 2번 자료 구조에 삽입하고 
# 2번 자료 구조에서 원소 x2 를 pop 한다 
# x(n-1) 을 N번 자료 구조에 삽입해서 x(n) 리턴 

# 길이 M 의 수열 C 를 가져와서 수열의 원소를 
# 앞에서부터 차례대로 queuestack 에 삽입한다 
# queuestack 에 넣을 원소들이 주어졌을 때 
# 해당 원소를 넣은 리턴값을 출력하는 문제 

# queuestack 은 queue or stack 으로 이루어진 자료 구조
# 각각의 자료 구조에는 처음에 하나의 원소가 들어 있고 
# 새로운 원소가 삽입될 때 저렇게 동작한다 
# Stack 에 넣는 건 의미 없으므로 Queue 만 고려 

from collections import deque
import sys 

n = int(sys.stdin.readline().strip()) # 자료 구조의 개수 
a = list(map(int, sys.stdin.readline().split())) # 0 Queue 1 Stack 
b = list(map(int, sys.stdin.readline().split())) # 자료 구조에 들어 있는 원소 
m = int(sys.stdin.readline().strip()) # 삽입할 수열의 길이 
c = list(map(int, sys.stdin.readline().split())) # queuestack 에 삽입할 원소

queue = deque()
results = [] # 결과를 저장할 리스트 

# Init Queuestack, Queue 인 경우에만 값 넣기 
for i in range(n):
    if a[i] == 0: 
        queue.appendleft(b[i])

for value in c:
    queue.append(value) # 새 값을 Queue 에 넣는다 
    # Queue 의 맨 앞 값을 빼서 result 에 추가한다 
    results.append(queue.popleft())

sys.stdout.write(" ".join(map(str, results)) + "\n")