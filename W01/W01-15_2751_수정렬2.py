# Quick 정렬 제출했더니 시간 초과 출력됨
# 0 <= N <= 1,000,000 (1은 1,000까지)

def mergeSort(a):
    # a 의 길이가 1 이하이면 끝
    if len(a) <= 1:
        return a
    
    # 반으로 나눠서, 앞 부분은 left 뒷 부분은 right 
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]

    # 모두 분해될 때까지 재귀 
    L = mergeSort(left)
    R = mergeSort(right)

    # 초기 설정은 모두 빈 값으로 선언
    i = j = 0
    result = []

    # i 와 j 가 길이보다 작을 때 while 
    # L[i] 와 R[j] 을 비교하여 result 에 append 
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
        
        # result 에 Left/ Right 합치기 
    result += L[i:]
    result += R[j:]
    return result
        
if __name__ == "__main__":

    num = int(input())
    num_list = [None] * num
    for i in range(num):
        num_list[i] = int(input())

    # mergeSort 로 정렬하고 Print 하기
    sorted_list = mergeSort(num_list)
    
    for i in sorted_list:
        print(i)
