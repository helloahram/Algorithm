# https://www.acmicpc.net/problem/10816

# N개의 숫자 카드를 가지고 있는 상황에서 M개의 카드가 주어졌을 때 
# 이 수가 적혀있는 숫자 카드를 몇 개 가지고 있는지 구하는 문제 
# 10,000,000 <= 숫자 <= 10,000,000

from collections import Counter
import sys

n = int(input())
old_cards = list(map(int, input().split()))
m = int(input())
new_cards = list(map(int, input().split()))

# 가지고 있는 카드의 갯수 계산 
card_count = Counter(old_cards)

# 찾아야 하는 카드를 돌며 가지고 있는 카드의 갯수 출력 
result = (str(card_count[card]) for card in new_cards)
# " " 로 구분하여 출력 
sys.stdout.write(" ".join(result) + "\n")

# 내일 다시 보기 