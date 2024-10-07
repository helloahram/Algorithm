#include <stdio.h>

int find_max(int *parr);             // 최대값을 찾는 함수
int sort_arr(int *parr, int *psort); // 정렬하는 함수

int main()
{
    int arr[10];        // 기존 배열
    int sorted_arr[10]; // 정렬 배열
    // 입력 받기
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", arr + i);
    }
    printf("%d\n", find_max(arr));

    return 0;
}

// 최대값을 찾는 함수
int find_max(int *parr)
{
    int max = -1;
    for (int i = 0; i < 10; i++)
    {
        if (max < parr[i])
        {
            max = parr[i];
        }
    }
    return max;
}