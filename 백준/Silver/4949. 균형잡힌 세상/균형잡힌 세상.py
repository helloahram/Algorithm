# https://www.acmicpc.net/problem/4949

# 영문 알파벳, 공백, 소괄호와 대괄호로 이루어져 있는 문자열에서
# 소괄호와 대괄호가 짝을 이루는지 판단하는 프로그램 

def is_vps(s):
    stack = []

    for c in s:
        if c in "([":
            stack.append(c)
        elif c == ")":
            # Stack 이 비었거나 짝이 맞지 않는 경우 NO 
            if not stack or stack[-1] != "(":
                return "no"
            # 짝이 맞으면 Pop 
            stack.pop()
        elif c == "]":
            if not stack or stack[-1] != "[":
                return "no"
            stack.pop()

    if not stack:
        return "yes"
    else:
        return "no"

if __name__ == '__main__':
    while True:
        line = input()
        if line == '.':
            break
        print(is_vps(line))
        