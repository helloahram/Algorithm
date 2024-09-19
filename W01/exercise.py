from collections import deque
import sys

queue = deque()

def push(x):
    queue.append(x)

def pop():
    if queue:
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