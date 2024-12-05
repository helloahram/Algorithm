# https://www.acmicpc.net/problem/18870

# 수직선 위에 위치한 N개의 좌표에 좌표 압축을 적용하려고 한다 
# Xi 를 좌표 압축한 Xi' 은 Xi > Xj 를 만족하는 서로 다른 좌표 Xj 의 개수와 같아야 한다 
# N개의 좌표를 좌표 압축한 결과를 공백 한 칸으로 구분해서 출력하는 문제 

# 예제를 보니까 좌표 압축은 제일 왼쪽에 있는 (작은) 점을 0 으로 시작해서 번호를 매기는 것
# 정렬 리스트를 만들어 정렬하고, 인덱스를 매핑해서, 압축을 하면 된다 

n = int(input()) 
points = list(map(int, input().split())) # 좌표 입력 

# 중복을 제거하고 좌표를 정렬하여 압축 기준이 될 새로운 리스트에 저장 
sorted_points = sorted(set(points)) 

# 압축된 좌표와 새로운 인덱스 매핑하여 딕셔너리 생성 
compress_map = {value: index for index, value in enumerate(sorted_points)}

# 입력 순서에 따라 각 좌표를 압축된 값으로 변환 
compress_points = [compress_map[point] for point in points]

# 결과를 공백으로 구분하여 출력 
print(' '.join(map(str, compress_points)))

# 나중에 꼭 다시 해 보기 