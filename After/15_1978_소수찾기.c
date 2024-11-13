// https://www.acmicpc.net/problem/1978

// 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램
// 제곱근까지만 나누면 시간 복잡도가 줄지 않을까?
/* 틀렸음 < is_prime 함수에서 for (int i = 3; i < sqrt(num); i += 2)
 i <= sqrt(num) 까지 for 문을 돌려야 한다 */

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/* 소수 여부를 구하는 함수 */
int is_prime(int num)
{
    if (num <= 1)
        return 0;
    if (num <= 2)
        return 1; /* 2는 소수 */
    if (num % 2 == 0)
        return 0; /* 2의 배수는 소수 아님 */

    /* 3부터 num의 제곱근까지 += 2 단위로 검사 */
    for (int i = 3; i <= sqrt(num); i += 2)
    {
        if (num % i == 0)
        {
            return 0; /* 나눠서 0 이 되면 소수 아님 */
        }
    }
    return 1; /* 나눠서 0 이 되는 숫자가 없으면 소수 */
}

int main()
{
    int n;
    scanf("%d", &n); // 입력 받을 숫자 입력 받기

    // 입력 받을 숫자의 배열
    int *nums = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &nums[i]); /* 숫자 입력 받기 */
    }

    int count = 0; // 소수의 개수를 저장할 변수
    for (int i = 0; i < n; i++)
    {
        if (is_prime(nums[i]))
            count++;
    }

    printf("%d\n", count);

    free(nums);
}