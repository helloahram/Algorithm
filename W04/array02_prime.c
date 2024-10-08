#include <stdio.h>

int main()
{
    int n;         // n까지의 소수 구하기
    int prime[20]; // 소수 배열
    int index = 1; // Index

    printf("범위 ; ");
    scanf("%d", &n);

    prime[0] = 2;
    for (int i = 3; i <= n; i += 2)
    {
        int is_prime = 1;
        for (int j = 2; j * j < i; j++)
        {
            if (n % i == 0)
            {
                is_prime = 0;
                break;
            }
        }
        if (is_prime)
        {
            prime[index++] = i;
        }
    }

    printf("소수 ; ");
    for (int i = 0; i < index; i++)
    {
        printf("%d ", prime[i]);
    }
    printf("\n");

    return 0;
}
