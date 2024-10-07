#include <stdio.h>

int add_number(int *parr);

int main()
{
    int arr[3];
    for (int i = 0; i < 3; i++)
        // scanf("%d", &arr[i]);
        scanf("%d", arr + i);

    add_number(arr);

    printf("%d %d %d\n", arr[0], arr[1], arr[2]);
    return 0;
}

// 모든 배열의 원소 +1 하는 함수
int add_number(int *parr)
{
    int i = 0;
    for (i = 0; i < 3; i++)
        parr[i] += 1;

    return 0;
}