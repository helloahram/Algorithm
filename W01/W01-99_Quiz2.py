# Quick Search

from typing import MutableSequence

def qSort(a: MutableSequence) -> None:
    # len(a) 가 1 이하인 경우 정렬 완료로 간주 
    if len(a) <= 1:
        return a
    # Pivot 을 맨 앞으로 선언 
    pivot = a[0]

    # Pivot 을 제외한 a 에서 pivot 와 비교하여 작은 수는 less 에 넣기
    less_than_pivot = [x for x in a[1:] if x <= pivot]
    # Pivot 을 제외한 a 에서 pivot 과 비교하여 큰 수는 greater 에 넣기 
    greater_than_pivot = [x for x in a[1:] if x > pivot]

    # 정렬한 less 와 greater, pivot 을 하나로 묶어서 return 
    # less 와 greater 가 각각 정렬이 끝날 때까지 재귀 실행 
    return qSort(less_than_pivot) + [pivot] + qSort(greater_than_pivot)

if __name__ == '__main__':
    # 공백으로 구분하여 문자열 입력 받기 
    num_list = list(map(int, input().split()))

    sorted_list = qSort(num_list)
    print(f" 정렬 완료 : {sorted_list}")