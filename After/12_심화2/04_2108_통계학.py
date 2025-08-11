# https://www.acmicpc.net/problem/2108

# 홀수인 N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램
# 첫째줄에 수의 개수 N과, 다음줄에 정수를 N개의 줄로 입력 (N <= 4000)

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값 (여러 개인 경우 두번째로 작은 값)
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())  # 수의 개수

num = [int(input()) for _ in range(n)]
# num = []  # N 개의 정수
# for i in range(n):
#     num.append(int(input()))

num.sort()  # num 정렬

# Counter(num) 로 등장 빈도를 계산하여 {값: 횟수} 딕셔너리 생성
cnt = Counter(num)
# 최대 빈도수 추출
max_freq = max(cnt.values())
# 최대 빈도를 가진 후보 값 추출
modes = sorted([v for v, c in cnt.items() if c == max_freq])
# 후보가 하나면 그대로 반환, 여러 개면 두번째 원소가 최빈값
mode = modes[0] if len(modes) == 1 else modes[1]

print(round(sum(num) / n))  # 산술평균
print(num[n // 2])  # 중앙값
print(mode)  # 최빈값
print(max(num) - min(num))  # 범위
