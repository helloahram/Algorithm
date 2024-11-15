// https://www.acmicpc.net/problem/24264

/* 아래 함수의 수행 횟수와 다항식 최고차항 차수 출력
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
} */

/* for 문이 2개 이므로 n*n 번 수행하고
n*n 의 최고차항은 2 */

#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);

    printf("%lld\n", n * n);
    printf("2\n");
}

/* 이거 틀렸대서 int 대신 long long 사용
int main()
{
    int n;
    scanf("%d", &n);

    printf("%d\n", n * n);
    printf("2\n");
}
*/