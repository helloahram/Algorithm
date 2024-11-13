// 24.10.30 WED
// 9x9 격자판에 쓰여진 자연수 또는 0 이 주어질 때
// 최대값을 찾고, 그 최대값이 몇 행 몇 열에 위치했는지 구하시오

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int max = -1;       // 최대값을 저장할 변수
    int indexi, indexj; // 최대값의 인덱스를 저장할 변수
    int i, j;           // 반복문 변수

    // 값을 저장할 행렬 메모리 할당
    int **arr = (int **)malloc(sizeof(int *) * 9);
    for (i = 0; i < 9; i++)
    {
        arr[i] = (int *)malloc(sizeof(int) * 9);
    }

    // 행렬 입력 받기
    for (i = 0; i < 9; i++)
    {
        for (j = 0; j < 9; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }

    // 최대값 찾기
    for (i = 0; i < 9; i++)
    {
        for (j = 0; j < 9; j++)
        {
            if (max < arr[i][j])
            {
                max = arr[i][j];
                indexi = i + 1;
                indexj = j + 1;
            }
        }
    }

    // 최대값과 인덱스 출력
    printf("%d\n", max);
    printf("%d %d\n", indexi, indexj);

    // 메모리 할당 해제
    for (i = 0; i < 9; i++)
        free(arr[i]);

    free(arr);

    return 0;
}