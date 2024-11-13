// https://www.acmicpc.net/problem/11653

/* 정수 N 이 주어졌을 때 소인수분해하는 프로그램 */
// 소수를 구하고, 작은 소수부터 계속 나누면 되겠지?

#include <stdio.h>
#include <math.h>

int main()
{
    int n;
    scanf("%d", &n);

    /* n 이 1인 경우 아무 것도 출력하지 않는다*/
    if (n == 1)
        return 0;

    for (int i = 2; i <= sqrt(n); i++)
    {
        while (n % i == 0)
        { /* n % i 로 나뉜다면 그 값을 출력하고
        그 값으로 나누어서 계속 반복 */
            printf("%d\n", i);
            n /= i;
        }
    }

    /* n 이 마지막 소수일 경우 출력 */
    if (n > 1)
        printf("%d\n", n);

    return 0;
}