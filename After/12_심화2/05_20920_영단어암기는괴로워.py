# https://www.acmicpc.net/problem/20920

# 아래 조건을 충족하고 길이가 M 이상인 단어들로 만들어진 단어장을 만든다
# 1 <= 단어의 개수 N <= 100,000, 1 <= 외울 단어의 길이 기준 M <= 10
# 1. 자주 나오는 단어일수록 앞에 배치한다
# 2. 해당 단어의 길이가 길수록 앞에 배치한다
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

import sys
from collections import Counter

# N 최대값이 100,000 이므로 빠른 입력 사용
input = sys.stdin.readline

n, m = map(int, input().split())

freq = Counter()  # 단어 빈도 계산을 위해 Counter 사용
for _ in range(n):
    w = input().strip()
    if len(w) >= m:  # 길이가 M 이상인 단어만 카운트
        freq[w] += 1  # Counter 가 자동으로 누적

# 정렬 우선순위 1) 빈도 내림차순 2) 길이 내림차순 3) 사전 순 오름차순
ordered = sorted(freq.keys(), key=lambda w: (-freq[w], -len(w), w))

print("\n".join(ordered))
