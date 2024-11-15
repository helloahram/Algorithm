// https://www.acmicpc.net/problem/24262

/* 아래 함수의 수행 횟수를 출력하고
수행 횟수를 다항식으로 나타냈을 때 최고차항의 차수를 출력한다
MenOfPassion(A[], n) {
    i = ⌊n / 2⌋;
    return A[i]; # 코드1
} */

// 이 함수는 n 과 무관하게 항상 1번 수행하고,
// 1 은 상수이므로 최고차항은 0 이다

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    /* n 과 무관하게 항상 1번 수행 */
    printf("1\n");
    /* 1 의 최고차항은 0 */
    printf("0\n");
}