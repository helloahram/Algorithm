# https://www.acmicpc.net/problem/2751

# N개의 수를 오름차순으로 정렬하는 프로그램 

import sys

n = int(input()) # 입력 받을 숫자의 개수 
numbers = [] # 입력 받을 숫자를 저장할 배열 

for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))

# 리스트 컴프리헨션으로 이렇게 표현할 수도 있다 
# numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

numbers.sort() # 정렬 

# map(str, numbers) numbers 리스트의 정수를 문자열로 변환
# "\n".join 문자열 리스트를 \n 로 연결하여 하나의 문자열로 만들기 
# sys.stdout.write() 최종 문자열 출력 
sys.stdout.write("\n".join(map(str, numbers))+ "\n")