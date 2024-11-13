# https://www.acmicpc.net/problem/11866
# N명의 사람이 앉아있고 순서대로 k번째 사람을 제거한다
# 한 사람이 제거되면 남은 사람들도 이루어진 원을 따라
# N명의 사람들이 모두 제거될 때까지 과정을 반복한다

# deque 로 구현 

from collections import deque

def josephus(n, k):
    queue = deque([i+1 for i in range(n)])
    result= []

    while queue:
        # k-1명의 사람을 앞에서 빼서 뒤로 다시 넣음
        queue.rotate(-(k-1))
        # k번째 사람을 제거하고 결과 리스트에 추가 
        result.append(queue.popleft)

    print("<"+ ", ".join(map(str, result)) + ">")

if __name__ == '__main__':
    n, k = map(int, input().split())
    josephus(n, k)