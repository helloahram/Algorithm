# https://www.acmicpc.net/problem/13241

# 두 수에 대하여 최소공배수를 구하는 프로그램 

# 50% 입력 중 A 와 B 는 1000 (10^3) 보다 작고
# 다른 50% 입력은 1000보다 크고 100,000,000 (10^8) 보다 작다 
# 큰 수 입력에 대하여 변수를 64비트 정수로 선언하시오 

import math

a, b = map(int, input().split())

# 유클리드 호제법으로 최소공배수 계산 및 출력 
print(a*b // math.gcd(a, b))