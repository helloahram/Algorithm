// 24.10.30 WED
// N * M 크기 두 행렬 A, B 가 주어졌을 때 두 행렬을 더하는 프로그램
// 행렬의 크기 N, M

#include <stdio.h>

int main()
{
    int n, m;               // 행렬의 크기 변수 선언
    int i, j;               // 반복문 변수 선언
    scanf("%d %d", &n, &m); // 행렬 크기 입력 받기

    // int *a = (int *)malloc(sizeof(int) * (n * m)); // 행렬 A
    // int *b = (int *)malloc(sizeof(int) * (n * m)); // 행렬 B
    int a[n][m];   // 행렬 A
    int b[n][m];   // 행렬 B
    int sum[n][m]; // 행렬합 sum

    // 행렬 A 입력 받기
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }
    // 행렬 B 입력 받기
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            scanf("%d", &b[i][j]);
        }
    }
    // 행렬 더하기
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            sum[i][j] = a[i][j] + b[i][j];
        }
    }
    // 결과 출력
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            printf("%d ", sum[i][j]);
        }
        printf("\n");
    }
    return 0;
}