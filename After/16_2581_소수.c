// https://www.acmicpc.net/problem/2581

/* 자연수 M과 N이 주어질 때, M 이상 N 이하 자연수 중 소수인 것을 모두 골라
이들 소수의 합과 최소값을 찾는 프로그램을 작성하시오 */

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int is_prime(int num)
{
    if (num <= 1) // 1 은 소수 아님
        return 0;
    if (num == 2) // 2 는 소수
        return 1;
    if (num % 2 == 0) // 짝수는 소수 아님
        return 0;
    for (int i = 3; i <= sqrt(num); i++)
    { // 나눠진다면 소수 아님
        if (num % i == 0)
            return 0;
    }
    // 안 나눠진다면 소수 아님
    return 1;
}

int main()
{
    int m, n;
    scanf("%d %d", &m, &n);

    // 소수를 저장할 배열
    int *primes = (int *)malloc(sizeof(int) * (n - m + 1));
    int index = 0; // 배열의 인덱스 변수
    int sum = 0;   // 배열의 총 합을 저장할 변수

    /* m 부터 n 까지, 소수라면 배열에 추가하고
    sum 에 합계를 누적한다 */
    for (int i = m; i <= n; i++)
    {
        if (is_prime(i))
        {
            primes[index] = i;
            sum += primes[index];
            index++;
        }
    }

    if (sum > 0)
    {                              /* 소수가 있는 경우 */
        printf("%d\n", sum);       // 소수의 합
        printf("%d\n", primes[0]); // 최소 소수 값
    }
    else
    { /* 소수가 없는 경우 */
        printf("-1\n");
    }

    free(primes);
    return 0;
}