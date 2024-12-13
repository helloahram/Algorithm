import sys
from collections import Counter

n = int(input())
old_cards = list(map(int, input().split()))
m = int(input())
new_cards = list(map(int, input().split()))

card_count = Counter(old_cards)

result = (str(card_count[card]) for card in new_cards)
sys.stdout.write(" ".join(result)+'\n')