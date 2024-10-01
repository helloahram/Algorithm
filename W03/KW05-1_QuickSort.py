# from typing import MutableSequence

# def qSort(a: MutableSequence) -> None:
#     if len(a) <= 1:
#         return a
#     pivot = a[0]

#     less_than_pivot = [x for x in a[1:] if x <= pivot]
#     greater_than_pivot = [x for x in a[1:] if x > pivot]

#     return qSort(less_than_pivot) + [pivot] + qSort(greater_than_pivot)

# if __name__ == '__main__':
#     num_list = list(map(int, input().split()))

#     sorted_list = qSort(num_list)
#     print(f" 정렬 완료 : {sorted_list}")

from typing import MutableSequence

def qSort(a: MutableSequence, left: int, right: int) -> None:
    if left >= right: # 재귀 종료 조건 
        return
    
    pl = left
    pr = right
    x = a[(left+right)//2] # Pivot 설정 

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl] # pl pr Swap
            pl += 1
            pr -= 1
    if left < pr: qSort(a, left, pr) # 왼쪽 부분 정렬 
    if pl < right: qSort(a, pl, right) # 오른쪽 부분 정렬 

if __name__ == '__main__':
    num = int(input()) # 입력할 숫자 

    arr = list(map(int, input().split())) # 숫자 배열 입력 받기 

    qSort(arr, 0, num-1) # Quick Sort 실행 

    print("정렬 완료", ' '.join(map(str, arr))) # 숫자 배열 한 줄로 출력 