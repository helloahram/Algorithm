# https://www.acmicpc.net/problem/14425

# N 개의 문자열로 이루어진 집합 S 가 있을 때 
# 입력으로 주어지는 M 개의 문자열 중에 S 에 포함된 개수를 구하는 문제 

# 알고리즘 분류 - 자료 구조, 문자열, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵 
# 집합 set 은 내부적으로 해시 테이블을 사용하여 구현되어 있으며
# 해시 테이블을 이용하면 원소를 빠르게 검색할 수 있다
# in 연산 사용 - O(1) 

n, m = map(int, input().split())

old_string = set() # old_string 을 집합으로 선언 

for _ in range(n): # old_string 문자열 입력 받기 
    old_string.add(input().strip())

count = 0
for _ in range(m):
    new_str = input().strip()
    # 입력 받은 문자열이 old_string 에 있으면 count++ 
    if new_str in old_string:
        count += 1

print(count)