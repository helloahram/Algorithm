# 나무의 수 n, 필요한 길이 m, 나무들의 높이 배열이 주어졌을 때 
# 적어도 m 미터를 가지고 가기 위해 절단기의 최대 높이를 구하는 문제

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 나무들의 높이를 오름차순으로 정렬 
trees.sort()

def get_tree(m, left, right, trees):

    # 이분 탐색을 통해 절단기 높이를 결정 
    while left <= right:
        # 절단기의 중간 높이 계산 
        mid = (left+right) // 2
    
        # 얻은 나무 길이의 합을 저장할 변수 초기화 
        # while 문을 돌 때마다 gets 값 갱신 필요 
        gets = 0

        # 얻게 된 나무 길이 계산
        # 절단기 높이 mid 보다 큰 나무에서 잘라낸 나무 길이를 gets 에 누적 
        for tree in trees:
            if tree > mid:
                gets += tree- mid 

        # 얻은 나무 길이 gets 가 원하는 나무 길이 m 보다 크면
        # 가능한 절단기 높이 result 를 mid 로 갱신하고
        # 절단기 높이를 더 높임 left = mid+1 
        if gets >= m:
            result = mid
            left = mid + 1
        # 얻은 나무 길이가 부족하면 절단기 높이를 더 낮춤 
        elif gets < m:
            right = mid - 1

    return result

# 절단기의 최대 높이는 가장 큰 나무의 높이, 최소 높이는 0 으로 설정하여
# get_tree 함수로 절단기 최대 설정 높이 계산 
print(get_tree(m, 0, max(trees), trees))