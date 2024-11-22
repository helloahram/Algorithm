# https://www.acmicpc.net/problem/2798

# 카드의 합이 21을 넘지 않는 한도 내에서 카드의 합을 최대한 크게 만드는 게임 
# N장의 카드에 써져 있는 숫자가 주어졌을 때 M에 최대한 가까운 3장의 합을 구하는 문제 

# Combinations 를 활용해서 해보기

from itertools import combinations

n, m = map(int, input().split()) # n 카드 개수 m 목표 합 
while True:
    cards = list(map(int, input().split())) # 카드 리스트 
    if len(cards) == n: break # n개 입력되면 OK 

# 3장의 카드를 뽑는 모든 조합의 합을 계산 
max_sum = 0
# combinations 로 cards 리스트에서 3개의 조합을 찾아 combo 에 저장한다 
for combo in combinations(cards, 3):
    s = sum(combo) # combo 의 모든 요소를 더해 s 에 저장한다 
    if s <= m: 
        max_sum = max(max_sum, s) # max_sum 재계산 

print(max_sum)