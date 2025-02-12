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
    return "YES" if not stack else "NO"

t = int(input())
for _ in range(t):
    bracket = input().strip()
    print(is_vps(bracket))