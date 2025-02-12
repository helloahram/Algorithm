# https://www.acmicpc.net/problem/4949

# 영문 알파벳, 공백, 소괄호와 대괄호로 이루어져 있는 문자열에서
# 소괄호와 대괄호가 짝을 이루는지 판단하는 프로그램 

# 아직 하는 중 

def is_vps(s):
    stack = []
    has_bracket = False # 괄호 여부 확인 

    for char in s:
        # Tuple 을 사용해서 비교
        if char == ('(', '['):
            stack.append(char)
            has_bracket = True
        elif char == (')', ']'):
            has_bracket = True
            if stack:
                # Stack 의 마지막 요소를 확인해서 짝이 맞는지 비교 
                top = stack[-1]
                if (char == ')' and top == '(') or (char == ']' and top == ']'):
                    stack.pop()
                else: # 짝이 맞지 않으면 NO 
                    return "NO"
            else:
                return "NO"
    
    return "YES" if not stack or not has_bracket else "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        testcase = input().strip()
        if testcase == '.':
            break
        print(is_vps(testcase))