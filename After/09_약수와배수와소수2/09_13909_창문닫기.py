# https://www.acmicpc.net/problem/13909

# N 개의 창문이 있고 N 명의 사람이 있을 때, 
# N 번째 사람은 N 의 배수의 창문을 열고 닫는다 
# 1 <= N <= 2,100,000,000 
# 마지막에 열려 있는 창문의 개수를 출력한다 

# 창문의 약수가 홀수이면 열려 있다 
# 대부분의 수는 약수가 짝수 개이다 
# 그래서 제곱수만 구하면 된다 

import math

n = int(input())

# 제곱수 구하고 출력하기 
result = math.isqrt(n)
print(result)