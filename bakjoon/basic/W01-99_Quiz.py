# Quick Sort - 분할 정복 알고리즘의 대표적인 예시
# (left+right)//2 로 Pivot 을 설정하고
# pl+1, pr-1 을 Pivot 과 비교하여 정렬한다 

# QuickSort 함수에 array 와 left, right 설정
# pivot 을 설정하고, left 부터 pivot 까지/ right 부터 Pivot 까지 비교한다

# pl 이 x 보다 작은 경우 pl+1 하며 찾고
# pr 이 x 보다 큰 경우 pr-1 하며 찾다가 
# 멈추면 pl 과 pr 을 변경해 준다
# Pivot 을 기준으로 정렬이 완료되면 왼쪽/ 오른쪽 나눠서 또 진행
# 만약 Pivot 의 위치가 변경될 경우 Pivot 의 위치는 바뀌지만 Pivot 은 그대로

# MutableSequence 변경 가능한 시퀀스 (요소 수정 가능)
# Sequence ; List, Tuple, Range, String, etc

from typing import MutableSequence

def qSort(a: MutableSequence, left: int, right: int) -> None:
    pl = left # 제일 왼쪽의 요소 
    pr = right # 제일 오른쪽의 요소 
    x = a[(left+right)//2] # Pivot 설정 

    # pl 이 pr 보다 작을 때 while 문이 돌아간다 
    while pl <= pr:
        # pl 이 가리키는 값이 Pivot 보다 작을 때 pl 을 뒤로 한 칸
        while a[pl] < x: pl += 1
        # pr 이 가리키는 값이 Pivot 보다 클 때 pr 을 뒤로 한 칸
        while a[pr] > x: pr -= 1
        # pl 과 pr 의 움직임이 멈추고 pl 이 pr 보다 앞에 있을 때
        # pl 이 가리키는 값과 pr 이 가리키는 값을 swap 하고
        # pl 뒤로 한 칸, pr 앞으로 한 칸 옮겨준다 
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    # pl 이 pr 보다 작은 경우 다시 while 문을 돈다
    # pl 이 pr 보다 큰 경우 while 문을 종료하고 
    # left < pr/ pl < right 의 조건을 충족할 때
    # 기존 Pivot 기준으로 앞부분과 뒷부분으로 나눠 다시 qSort 진행 
    if left < pr: qSort(a, left, pr)
    if pl < right: qSort(a, pl, right)

def Quick_Sort(a: MutableSequence) -> None:
    qSort(a, 0, len(a)-1)

if __name__ == '__main__':
    print(" 배열 입력 받기 ")
    num = int(input())

    x = [None] * num # 배열 개수 입력 받고 None 으로 초기화하기 

    for i in range(num): # 배열 하나씩 입력 받기
        x[i] = int(input(f'[x{i}]: '))

    Quick_Sort(x) # Quick Sort 진행 

    print(" 정렬 완료 ")
    for i in range(num): # 정렬 완료 후 차례로 Print 
        print(f'[x{i}]: = {x[i]}')
