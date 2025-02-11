import math
import sys 

def push(stack, x):
    stack.append(x)
    return stack
    
def pop(stack):
    if stack:
        print(stack[-1])
        stack.pop()
    else:
        print("-1")
    
def length(stack):
    print(len(stack))

def is_empty(stack):
    if stack:
        print("0")
    else:
        print("1")

def peek(stack):
    if stack:
        print(stack[-1])
    else:
        print("-1")

if __name__ == '__main__':
    n = int(input())
    stack = []

    for i in range(n):
        c = sys.stdin.readline().split()
        
        if c[0] == '1':
            push(stack, int(c[1]))
        elif c[0] == '2':
            pop(stack)
        elif c[0] == '3':
            length(stack)
        elif c[0] == '4':
            is_empty(stack)
        elif c[0] == '5':
            peek(stack)