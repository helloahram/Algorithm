# 반으로 나눠서 왼쪽 부분의 시작을 left, 
# 오른쪽 부분의 시작을 mid+1 
# 병합 배열의 시작도 left 로 초기값을 준다
# 그리고 left right 차례로 하나씩 비교하기 

# 분할된 부분을 병합하는 함수
def merge_sort(a):
    if len(a) <= 1:
        return a

    # 분할된 부분을 정렬하는 함수 
    def merge(left, right):
        sorted_list = []
        i = j = 0

        # left right 비교하여 sorted_list 에 append 하기 
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        while i < len(left):
            sorted_list.append(left[i])
            i += 1
        while j < len(right):
            sorted_list.append(right[j])
            j += 1

        return sorted_list
    
    mid = len(a) // 2
    left_half = merge_sort(a[:mid])
    right_half = merge_sort(a[mid:])
    return merge(left_half, right_half)
    
if __name__ == '__main__':
    num = int(input())
    num_list = [None] * num

    for i in range(num):
        num_list[i] = int(input())

    sorted_list = merge_sort(num_list)
    print(" 결과 출력 ")

    for i in sorted_list:
        print(i)
