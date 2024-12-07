# https://www.acmicpc.net/problem/10815 

# 숫자가 적힌 카드 N 개가 있을 때 주어진 숫자 M 개가
# N 개의 카드에 있으면 1, 아니면 0 을 출력하는 문제 
# 숫자 카드의 개수 1 <= N, M <= 500,000
# 적혀있는 수 -10,000,000 <= 수 <= 10,000,000 

# 알고리즘 분류는 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵 
# 정렬하고 이분 탐색을 해봐야겠다 

import sys

n = int(input())
# 카드 리스트를 집합으로 변환 - 집합은 중복 자동 제거 
old_cards = set(map(int, sys.stdin.readline().split()))
m = int(input())
# 찾아야 하는 카드들은 순서가 중요하니 리스트로 저장 
new_cards = list(map(int, sys.stdin.readline().split()))

# new_cards 리스트의 각 원소 확인
# old_cards 에 존재하면 1, new_cards 에만 있으면 0 추가 
results = [1 if q in old_cards else 0 for q in new_cards]

# 결과를 공백으로 구분하여 출력 
print(' '.join(map(str, results)))