# https://www.acmicpc.net/problem/10989

# N개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램 
# 1 <= N <= 10,000,000, 시간 제한 5초 메모리 제한 8MB

# 수 정렬하기2 코드를 고대로 제출했는데, 메모리 제한이 떴다
# 입력이 매우 크고 범위가 제한적일 때 등장 횟수를 기록하는 방법도 있다고 한다 
# 등장 횟수를 배열로 저장하고 출력하는 방법을 사용해 보기로 했다  

import sys

n = int(sys.stdin.readline().strip()) # 입력 받을 숫자 개수 

# MAX_VALUE = 10000 # 최대 입력할 수 있는 숫자의 개수 
# 불필요한 변수 사용 줄이기 1
count = [0] * (10001) # 등장 횟수를 저장하는 배열 

# 등장 횟수 카운트 
for _ in range(n):
    # num = int(sys.stdin.readline().strip())
    # count[num] += 1
    # 불필요한 변수 사용 줄이기 2 입력 즉시 배열에 저장 
    count[(int(sys.stdin.readline().strip()))] += 1

# 등장한 횟수만큼 출력 ( * count[num] )
for num in range(1, 10001):
    if count[num] > 0:
        # sys.stdout.write((str(num) + "\n") * count[num])
        print(f"{num}\n" * count[num], end='')

# 아직 메모리 초과임 