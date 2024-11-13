// 소수의 개수 구하기

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int is_prime(int num)
{
    if (num <= 1)
        return 0;
    if (num == 2)
        return 1;
    if (num % 2 == 0)
        return 0;

    for (int i = 3; i < sqrt(num); i += 2)
    {
        if (num % i == 0)
            return 0;
    }
    return 1;
}

int main()
{
    int n;
    scanf("%d", &n);

    int *nums = (int *)malloc(sizeof(int) * n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &nums[i]);
    }

    int count = 0;
    for (int i = 0; i < n; i++)
    {
        if (is_prime(nums[i]))
            count++;
    }

    printf("%d\n", count);
    free(nums);
}
