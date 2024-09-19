# 정수를 저장하는 큐를 구현한 다음,
# 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오

# push x - 정수 x 를 큐에 넣는 연산
# pop - 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력
#       만약 큐에 들어있는 정수가 없는 경우에는 -1 을 출력
# size - 큐에 들어있는 정수의 개수를 출력
# empty - 큐가 비어있으면 1, 아니면 0 출력
# front - 큐의 가장 앞에 있는 정수 출력, 없으면 -1 출력 
# back - 큐의 가장 뒤에 있는 정수 출력, 없으면 -1 출력

from collections import deque
import sys

queue = deque()

def push(x):
    queue.append(x)

def pop():
    if queue:
        # firstpang = queue[0]
        # del queue[0]
        # print(firstpang)
        print(queue[0])
        queue.popleft()
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    print(0 if queue else 1)

def front():
    print(queue[0] if queue else -1)

def back():
    print(queue[-1] if queue else -1)

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        # c = input().split()
        # input() 은 시간 초과가 떠서, sys.stdin.readline() 사용 
        # rstrip() 문장 끝의 개행 문자를 없애기 
        # split() 공백을 기준으로 명령어를 분리하여 리스트로 처리 
        c = sys.stdin.readline().rstrip().split()

        if c[0] == 'push':
            push(int(c[1]))
        elif c[0] == 'pop':
            pop()
        elif c[0] == 'size':
            size()
        elif c[0] == 'empty':
            empty()
        elif c[0] == 'front':
            front()
        elif c[0] == 'back':
            back()