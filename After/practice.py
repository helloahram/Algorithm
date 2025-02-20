from collections import deque

n = int(input())
balloon = deque(enumerate(map(int, (input().split())), start=1))
result = []

num, move = balloon.popleft()
result.append(num)

while balloon:
    if move > 0:
        balloon.rotate(-(move-1))
    else:
        balloon.rotate(-move)

    num, move = balloon.popleft()
    result.append(num)

print(*result)