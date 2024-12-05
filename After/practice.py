# 좌표 크기 기준으로 0 부터 번호 매기기 

# 정렬 리스트를 만들어서 정렬을 해주고
# 매칭해주면 되지!

n = int(input())

points = list(map(int, input().split()))

sorted_point = sorted(set(points))

compress_map = {value: index for index, value in enumerate(sorted_point)}

compress_points = [compress_map[point] for point in points]

print(' '.join(map(str, compress_points)))