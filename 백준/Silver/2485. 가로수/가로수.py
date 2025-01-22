# https://www.acmicpc.net/problem/2485

# 심어져 있는 가로수의 위치가 주어질 때, 모든 가로수가 같은 간격이 되도록
# 새로 심어야 하는 가로수의 최소수를 구하는 프로그램을 작성하라 

# 첫째줄에 이미 심어져 있는 가로수의 수 N 이 주어진다 
# 둘째줄부터 N개의 줄에는 각 줄마다 심어져 있는 가로수의 위치가 양의 정수로 주어지고
# 가로수의 위치를 나타내는 정수는 1,000,000,000 이하이다 


import math 
from functools import reduce

n = int(input()) # 이미 심어져 있는 가로수의 갯수 
m = [int(input()) for _ in range(n)] # 가로수의 위치 

# 가로수들의 간격 계산 
distances = [m[i+1] - m[i] for i in range(n-1)]

# 최대공약수 계산 
gcd = reduce(math.gcd, distances)

# 추가로 심어야 하는 가로수 계산 
trees_to_add = sum((dist // gcd-1) for dist in distances)

print(trees_to_add) # 결과 출력 