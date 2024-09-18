# m 개의 정수 X 가 n 개의 정수 a[] 안에 존재하는지 찾는 프로그램 
# x 찾을 정수 left 왼쪽 경계 right 오른쪽 경게 


# 이분 탐색 함수 
def binarySearch(x, left, right, a):
    while left <= right:
        # a 의 중간값 계산 
        mid = (left+right) // 2

        # 값을 찾은 경우 1 반환
        # 찾는 값이 더 크면 오른쪽 반, 작으면 왼쪽 반 탐색 
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            left = mid+1
        elif x < a[mid]:
            right = mid-1

    # 값을 찾지 못한 경우 0 반환
    return 0


if __name__ == '__main__':
    # n 배열의 크기, a n 개의 정수 배열 입력 받기 
    n = int(input())
    a = [int(i) for i in input().split()]

    # a 에 n 개의 정수가 입력되지 않으면 오류 발생
    if len(a) != n:
        raise ValueError(f"Expected {n} integers")

    # m 배열의 크기, arr m 개의 정수 배열 입력 받기 
    m = int(input())
    arr = [int(i) for i in input().split()]

    # arr 에 m 개의 정수가 입력되지 않으면 오류 발생
    if len(arr) != m:
        raise ValueError(f"Expected {m} integers")
    
    # n = 5
    # a = [5, 1, 4, 2, 3]
    # m = 5
    # arr = [1, 3, 7, 5, 9]

    # a 배열을 이분 탐색으로 나누기 전에 먼저 오름차순 정렬부터 하기
    a.sort()
    result = []

    # arr 의 각 정수에 대해 이분 탐색 수행하여 결과 저장하기 
    for x in arr:
        result.append(str(binarySearch(x, 0, len(a)-1, a)))

    # 결과를 공백으로 구분하여 출력 
    print(' '.join(result))