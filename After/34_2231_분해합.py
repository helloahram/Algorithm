# https://www.acmicpc.net/problem/2231

# 자연수 N 의 분해합은 N 과 N 을 이루는 각 자리수의 합을 의미한다 
# 어떤 자연수 M 의 분해합이 N 인 경우, M 을 N 의 생성자라 한다 
# 자연수 N 이 주어졌을 때, N 의 가장 작은 생성자를 구해내는 프로그램을 작성하시오 
# 생성자가 없는 경우에는 0 을 출력한다 

# 백의자리 + 십의자리 + 일의자리 + 원래숫자 = n 인 조합을 찾기 

from itertools import combinations

n = int(input())


a = n // 100 # 백의 자리
b = (n % 100) // 10 # 십의 자리
c = n % 10 # 일의 자리 

