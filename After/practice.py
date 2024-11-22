from itertools import combinations

n, m = map(int, input().split())
while True:
    cards = list(map(int, input().split()))
    if len(cards) == n: break

max_sum = 0
for combo in combinations(cards, 3):    
    s = sum(combo)
    if s <= m:
        max_sum = max(max_sum, s)

print(max_sum)