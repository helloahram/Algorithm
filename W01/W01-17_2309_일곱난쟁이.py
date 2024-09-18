# 일곱 난쟁이 키의 합이 100 일 때, 돌아온 9명 중에
# 일곱 난쟁이를 찾아서 오름차순으로 출력하는 프로그램

import itertools

# 돌아온 난쟁이 N 으로 설정하기 
N = 9

# N 만큼의 숫자를 엔터로 입력 받기 
height_list = []
for i in range(N):
    height_list.append(int(input().strip()))

# 9개 중 7개를 고르는 조합을 생성 
combinations = itertools.combinations(height_list, 7)

# 조합 comb 의 합이 100일 때 result 에 값 저장하고
# result 리스트의 값을 바로 순회하여 height 출력 
for comb in combinations:
    if sum(comb) == 100:
        result = sorted(comb)
        for height in result:
            print(height)
        break

# sort 대신 sorted 를 쓴 이유는,
# itertools.combination() 에서 생성된 조합은 튜플이기 때문!
# sort 쓰려면, comb = list(comb), comb.sort() 하면 됨