# https://www.acmicpc.net/problem/1735

# 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램
# 분수 합을 구하고 최대공약수로 나눠서 계산하면 되겠다 

import math 

a, b = map(int, input().split())
c, d = map(int, input().split())

e = (a * d) + (b * c) # 분수 합의 분자 
f = b * d # 분수 합의 분모 

# 최대공약수로 분자 분모 나누기 
gcd = math.gcd(e, f)
e //= gcd
f //= gcd

# 분자 분모 출력
print(e, f)