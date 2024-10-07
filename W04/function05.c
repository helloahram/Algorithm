// 문제 5
// 특정한 수 N 을 입력받아서 N 을 소인수분해한 결과가
// 출력되게 해보세요 (난이도 : 中)
// 예) factorize(10); 출력결과 : 2 × 5
// factorize(180); 출력결과 : 2 × 2 × 3 × 3 × 5

#include <stdio.h>

void factorize(int n)
{
    while (n % 2 == 0)
    {
        printf("2");
        n /= 2; // 2 로 계속 나누기
        if (n > 1)
        {
            printf(" X ");
        }
    }

    // 3 이상부터는 제곱근까지만 나누기
    for (int i = 3; i * i < n; i += 2)
    {
        while (n % i == 0)
        {
            printf("%d", i);
            n /= i;
            if (n > 1)
            {
                printf(" X ");
            }
        }
    }

    // n 이 2보다 큰 소수인 경우
    if (n > 2)
    {
        printf("%d", n);
    }
    printf("\n");
}

int main()
{
    int num = 0;
    scanf("%d", &num);

    factorize(num);
}