// 문제 4
// N 값을 입력 받아서 1 부터 N 까지의 소수의 개수를
// 출력하는 함수를 제작해보세요. (난이도 : 下)

#include <stdio.h>

int find_prime(int n)
{
    int count = 0;

    for (int i = 2; i <= n; i++)
    {
        int is_prime = 1; // 소수 여부 판정

        for (int j = 2; j * j <= i; j++) // 제곱근까지 확인
        {
            if (i % j == 0)
            {
                is_prime = 0;
                break;
            }
        }
        if (is_prime)
            count += 1;
    }
    return count;
}

int main()
{
    int num;
    scanf("%d", &num);

    printf("%d\n", find_prime(num));
}