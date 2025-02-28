# https://www.acmicpc.net/problem/1010 

# 서쪽에 N 개 동쪽에 M 개 장소를 다리로 연결할 때 
# 겹쳐지지 않고 최대한 많이 지을 수 있는 경우의 수 

# Combination

import sys
import math 

t = int(sys.stdin.readline().strip())
result = []

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    # M 개의 사이트 중에서 N 개를 선택
    result.append(math.comb(m, n))

sys.stdout.write("\n".join(map(str, result)) + "\n")