// https://www.acmicpc.net/problem/15894

/* 한 변의 길이가 1인 정사각형을 한 개씩 더 추가해서 붙여 나간다
가장 아랫 부분의 정사각형이 n개가 되었을 때, 실선으로 이루어진
도형의 둘레의 길이를 구하는 문제 */

// 4개까지 해봤는데 그냥 X4 가 되고 있다

#include <stdio.h>

int main()
{
    /* long long 타입으로 써야지 */
    long long n;
    scanf("%lld", &n);

    printf("%lld\n", n * 4);

    /* 기존에 작성한 코드
    int n;
    scanf("%d", &n);

    printf("%d\n", n * 4);
    */
}