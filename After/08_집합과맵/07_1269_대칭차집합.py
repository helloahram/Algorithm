# https://www.acmicpc.net/problem/1269

# 자연수를 원소로 갖는 공집합이 아닌 두 집합 A 와 B 가 있을 때 
# 두 집합의 대칭 차집합의 원소의 개수를 출력하는 문제 

# A, B 원소 개수와 원소 입력 받기 
n, m = map(int, input().split())

a = set(input().split())
b = set(input().split())

difference = a ^ b
print(len(difference))

# a 에는 있고 b 에는 없는 원소를 구하려면 a - b 하면 됨!
# 그래서 a ^ b 대신, (a-b) | (b-a) 로 구할 수 있다 