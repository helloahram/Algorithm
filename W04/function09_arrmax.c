#include <stdio.h>

void sort_arr(int *parr, int size); // 배열 정렬 함수 선언

int main()
{
    int arr[10]; // 배열 선언
    int i = 0;
    // 배열 입력 받기
    for (i = 0; i < 10; i++)
    {
        scanf("%d", arr + i);
    }

    sort_arr(arr, 10); // 배열 정렬 함수 호출

    // 정렬한 배열 출력하기
    printf("Sorted Array ");
    for (i = 0; i < 10; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// 정렬 함수
void sort_arr(int *parr, int size)
{
    for (int i = 0; i < size - 1; i++)
    {
        int max_index = i; // 최대값 인덱스 초기화
        // i 다음부터 size 까지 돌며 최대값 비교
        for (int j = i + 1; j < size; j++)
        {
            if (parr[j] > parr[max_index])
            {
                max_index = j;
            }
        }
        // max_index != i 면 최대값이 변경된 것이므로 교환
        if (max_index != i)
        {
            int temp = parr[i];
            parr[i] = parr[max_index];
            parr[max_index] = temp;
        }
    }
}