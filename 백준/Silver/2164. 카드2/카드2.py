# https://www.acmicpc.net/problem/2164

# 1부터 N까지 번호가 붙어 있는 카드가 있을 때 
# 제일 위에 있는 카드를 바닥에 버리고
# 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다 
# N이 주어졌을 때 제일 마지막에 남게 되는 카드를 구하는 프로그램 

# 처음에 popleft 하고, 다음 popleft 한걸 append 하면 되겠다

from collections import deque

n = int(input())
cards = deque(range(1, n+1))

while len(cards) > 1:
    cards.popleft()
    temp = cards.popleft()
    cards.append(temp)

print(cards[0])