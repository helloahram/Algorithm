# https://www.acmicpc.net/problem/15439

# 상의 N 벌과 하의 N 벌이 있을 때 
# 서로 다른 색상인 조합은 총 몇 가지인지 구하는 프로그램 

# n X n-1 

n = int(input())

print(n * (n-1))