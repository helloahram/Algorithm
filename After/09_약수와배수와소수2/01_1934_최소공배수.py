# https://www.acmicpc.net/problem/1934

# 두 자연수 A 와 B 의 최소 공배수를 구하는 프로그램
# 첫째 줄부터 T 개의 줄에 최소공배수를 입력받은 순서대로 출력
# math 의 lcm 를 활용하면 간단하다 

import math
import sys
input = sys.stdin.readline # 한 줄씩 입력 받기 

t = int(input().strip()) # Test Case 갯수 
num = [] # 최소공배수들을 저장할 리스트  

# t번 반복하며 a, b 입력 받고 lcm 을 리스트에 저장하기
for _ in range(t):
    a, b = map(int, input().split())
    num.append(math.lcm(a, b))
    # 또는 유클리드 호제법을 사용할 수도 있음 
    # lcm = (a * b) // math.gcd(a, b)

# num 리스트의 각 숫자를 str 함수를 사용하여 문자열로 변환하고
# join() 을 사용해 변환된 문자열 요소 사이에 줄바꿈 \n 삽입 
print("\n".join(map(str, num)))

# 출력을 아래 방식으로 해도 됨
# for i in range(t):
#     print(num[i])