# https://www.acmicpc.net/problem/10773

# 0에서 1,000,000 사이의 정수가 한 개씩 주어진다 
# 정수가 "0"일 경우 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다 
# 최종적으로 적어낸 수의 합을 출력하는 프로그램 

import sys

if __name__ == '__main__':
    k = int(input()) # 입력 개수 
    stack = [] 

    for _ in range(k):
        # 입력 값을 정수로 변환하여 저장 
        c = int(sys.stdin.readline().strip())

        if c == 0:
            if stack:
                stack.pop()
        else:
            stack.append(c)

    print(sum(stack))
