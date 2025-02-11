# https://www.acmicpc.net/problem/28278

# 정수를 저장하는 스택을 구현한 다음, 
# 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오 

# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한

# 출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력 

import sys

def push(stack, n):
    stack.append(n)

def pop(stack):
    if stack:
        print(stack[-1])
        stack.pop()
    else:
        print('-1')
    
def length(stack):
    print(len(stack))

def is_empty(stack):
    print(0 if stack else 1)
    
def peek(stack):
    print(stack[-1] if stack else '-1')
    
if __name__ == '__main__':
    n = int(input())
    stack = []

    for _ in range(n):
        # 입력을 리스트로 받아 조건문에서 처리 
        i = sys.stdin.readline().split()

        if i[0] == '1':
            push(stack, int(i[1]))
        elif i[0] == '2':
            pop(stack)
        elif i[0] == '3':
            length(stack)
        elif i[0] == '4':
            is_empty(stack)
        elif i[0] == '5':
            peek(stack)