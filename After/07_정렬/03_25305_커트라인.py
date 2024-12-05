# https://www.acmicpc.net/problem/25305 

# 시험에 응시한 N명 중 상을 받는 사람 k명이 있을 때
# 상을 받는 사람 중에 제일 낮은 점수를 구하는 문제 

# 시험 점수를 내림차순으로 정렬하고 k-1 점수 출력하면 되겠지?

# 시험에 응시한 n, 상을 받는 k 변수 입력 받기 
n, k = map(int, input().split())
scores = list(map(int, input().split()))

# 시험 점수 내림차순 정렬 
scores.sort(reverse=True)

# k번째 점수 출력 
print(scores[k-1])

# 이렇게 입력 + 정렬 + 출력을 한꺼번에 할 수도 있다 
# print(sorted(map(int, input().split()), reverse=True)[k - 1])