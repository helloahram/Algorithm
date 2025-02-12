# https://www.acmicpc.net/problem/9012

# 괄호의 모양이 바르게 구성된 문자열인 
# 올바른 괄호 문자열 Valid PS, VPS 을 판단하여
# 결과를 YES or NO 로 나타내는 프로그램 

# stack 에 넣어서 ) 가 나오면 ( 가 있는지 확인하면 되겠다
# ( 가 나오면 Push, ) 가 나오면 pop 

def is_vps(s):
    stack = []
    for char in s:
        # ( 이면 Stack 에 추가하기 
        if char == '(':
            stack.append(char)
        elif char == ')':
            # Stack 이 비어 있지 않으면 짝을 맞추기 위해 Pop
            if stack:
                stack.pop()
            # Stack 이 비어 있는데 ) 가 나오면 VPS 아님
            else:
                return "NO"
    # stack 이 남아 있으면 NO, 비어 있으면 YES
    return "YES" if not stack else "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        # Strip 으로 입력 받은 문자열에서 불필요한 공백 제거 
        bracket = input().strip()
        print(is_vps(bracket))