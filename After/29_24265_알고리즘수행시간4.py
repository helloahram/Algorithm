# https://www.acmicpc.net/problem/24265

# 아래 함수의 수행 횟수와 다항식 최고차항 차수 출력
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

# 3 이랑 달라진 건 i 가 n-1 까지, j 가 i+1 부터 
# 그러면 i 는 n-1 번 돌고, j 는 n-i 번 돈다 

n = int(input())

execution = (n * (n-1)) // 2
degree = 2

print(execution)
print(degree)

