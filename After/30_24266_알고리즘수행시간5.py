# https://www.acmicpc.net/problem/24266 

# 아래 함수의 수행 횟수와 다항식 최고차항 차수 출력
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# for 문 3개니까 n*n*n, 3차

n = int(input())

# execution = n*n*n
execution = n**3
degree = 3

print(execution)
print(degree)