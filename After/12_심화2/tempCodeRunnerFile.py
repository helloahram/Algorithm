# https://www.acmicpc.net/problem/1037

# 양수 A 가 N 의 진짜 약수가 되려면 
# N 이 A 의 배수이고, A 가 1 과 N 이 아니어야 한다 
# N 의 진짜 약수가 주어질 때 N 을 구하는 문제 

# 그러면 진짜 약수의 최소값과 최대값을 곱하면 N 이 됨

t = int(input())

divisor = list(map(int, input().split()))

print(min(divisor) * max(divisor))