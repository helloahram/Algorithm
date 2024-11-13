#  https://www.acmicpc.net/problem/11279
#  24.10.28 MON

# * 최대 힙
# 1. 배열에 자연수 x 를 넣는다
# 2. 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거한다
# 프로그램은 처음에 비어 있는 배열에서 시작하게 된다

#  연산의 개수 N 연산의 정보를 나타내는 x
#  x 가 자연수라면 배열에 넣기 + 배열에 추가하고, 정렬하기
#  x 가 0 이라면 배열에서 가장 큰 값 출력하고 배열에서 제거 

import sys
import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        heapq.heappush(self.heap, -x)

    def delete_max(self):
        if not self.heap:
            return 0
        return -heapq.heappop(self.heap)
    
def main():
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    # 나머지는 내일 해야지 총총,...