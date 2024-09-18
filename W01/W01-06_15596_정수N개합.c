#include <stdio.h>

long long sum(int *a, int n)
{
    long long total = 0;
    for (int i = 0; i < n; i++)
    {
        total += a[i];
    }
    return total;
}

// int main()
// {
//     int n = 3;
//     int a[] = {5, 6, 7};
//     long long result = sum(a, n);
//     printf("%lld \n", result);
// }

int main()
{
    int n = 0;

    printf("배열의 크기를 입력하세요: ");
    scanf("%d", &n);

    int a[n]; // 크기가 n인 배열 선언

    // 사용자로부터 배열의 값 입력받기
    printf("배열의 값을 입력하세요:\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    // sum 함수 호출 및 결과 출력
    long long result = sum(a, n);
    printf("배열의 합: %lld\n", result);

    return 0;
}