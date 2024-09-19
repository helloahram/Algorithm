# 정수를 저장하는 스택을 구현한 다음, 
# 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오 

# push X - 정수 X 를 스택에 넣는 연산
# pop - 스택에서 가장 위에 있는 정수를 빼고, 그 수 출력
#       만약 들어있는 정수가 없는 경우에는 -1 출력 
# size - 스택에 들어있는 정수 개수 출력
# empty - 스택이 비어있으면 1, 아니면 0 출력 
# top - 스택의 가장 위에 있는 정수 출력, 없으면 -1 

stack = []

def push(x):
    stack.append(x)

def pop():
    # print(stack.pop() if stack else -1)
    if stack:
        lastpang = stack[-1]
        del stack[-1]
        print(lastpang)
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    print(0 if stack else 1)

def top():
    print(stack[-1] if stack else -1)

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        c = input().split()

        if c[0] == 'push':
            push(int(c[1]))
        elif c[0] == 'pop':
            pop()
        elif c[0] == 'size':
            size()
        elif c[0] == 'empty':
            empty()
        elif c[0] == 'top':
            top()