# 가지고 있는 숫자이면 1, 아니면 0 출력 

n = int(input())
old_cards = set(map(int, input().split()))
m = int(input())
new_cards = list(map(int, input().split()))

result = [1 if q in old_cards else 0 for q in new_cards]

print(' '.join(map(str, result)))