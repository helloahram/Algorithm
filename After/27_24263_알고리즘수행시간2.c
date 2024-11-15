// https://www.acmicpc.net/problem/24263

/* 아래 함수의 수행 횟수와 다항식 최고차항 차수 출력
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
} */

/* 1 to n 이므로 n 번 수행되고
n 의 최고차항은 1 이다 */

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    printf("%d\n", n);
    printf("1\n");
}