n = int(input())

# 정렬할 수를 담음
num_list = []

for i in range(n):
    num_list.append(int(input()))
num_list.sort()

print(*num_list)
