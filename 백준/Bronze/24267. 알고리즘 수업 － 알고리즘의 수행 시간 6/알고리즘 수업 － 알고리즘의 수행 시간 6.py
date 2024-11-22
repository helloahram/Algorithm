# https://www.acmicpc.net/problem/24267

# 아래 함수의 수행 횟수와 다항식 최고차항 차수 출력
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# k 는 j+1 부터 n 까지, n-j
# j 는 i+1 부터 n-1 까지, n-i-1
# i 는 1부터 n-2 까지
# 이 구조는 1부터 n까지 숫자 중 3개를 선택하는 조합의 수와 같다 

n = int(input())

execution = ((n * (n-1) * (n-2)) // 6)
degree = 3

print(execution)
print(degree)