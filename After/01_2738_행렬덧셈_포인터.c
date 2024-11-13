// 24.10.30 WED
// N * M 크기 두 행렬 A, B 가 주어졌을 때 두 행렬을 더하는 프로그램
// 행렬의 크기 N, M

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m;               // 행렬 크기 변수 선언
    scanf("%d %d", &n, &m); // 행렬 크기 입력 받기
    int i, j;               // 반복문 변수 선언

    // 각 행을 가리킬 포인터를 위한 메모리 할당
    int **a = (int **)malloc(n * sizeof(int *));
    int **b = (int **)malloc(n * sizeof(int *));
    int **sum = (int **)malloc(n * sizeof(int *));

    // 각 행에 해당하는 실제 데이터를 저장할 공간 할당
    for (i = 0; i < n; i++)
    {
        a[i] = (int *)malloc(m * sizeof(int));
        b[i] = (int *)malloc(m * sizeof(int));
        sum[i] = (int *)malloc(m * sizeof(int));
    }

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

    // 메모리 할당 해제
    for (i = 0; i < n; i++)
    {
        free(a[i]);
        free(b[i]);
        free(sum[i]);
    }

    free(a);
    free(b);
    free(sum);

    return 0;
}