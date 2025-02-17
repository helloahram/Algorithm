def is_vps(s):
    stack = []
    bracket_map = {')':'(', ']':'['}

    for char in s:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or stack[-1] != bracket_map[char]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"


while True:
    line = input()
    if line == '.':
        break
    print(is_vps(line))