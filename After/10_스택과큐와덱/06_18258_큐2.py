# https://www.acmicpc.net/problem/18258

# 정수를 저장하는 큐를 구현한 다음
# 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오 

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 
# 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 
# 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque
import sys 

def push(queue, x):
    queue.append(x)

def pop(queue):
    if queue:
        print(queue[0])
        queue.popleft()
    else:
        print(-1)

def size(queue):
    print(len(queue))

def empty(queue):
    print(0 if queue else 1)

def front(queue):
    print(queue[0] if queue else -1)

def back(queue):
    print(queue[-1] if queue else -1)

if __name__ == '__main__':
    t = int(input())
    queue = deque()

    for _ in range(t):
        c = sys.stdin.readline().strip().split()

        if c[0] == 'push':
            queue.append(int(c[1]))
        elif c[0] == 'pop':
            pop(queue)
        elif c[0] == 'size':
            size(queue)
        elif c[0] == 'empty':
            empty(queue)
        elif c[0] == 'front':
            front(queue)
        elif c[0] == 'back':
            back(queue)