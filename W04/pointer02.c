#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *arr[3];
    int i, j;

    for (i = 0; i < 3; i++)
    {
        arr[i] = (int *)malloc(5 * sizeof(int));
    }

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 5; j++)
        {
            arr[i][j] = 10 * (i + 1) + j;
        }
    }

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 5; j++)
        {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    for (i = 0; i < 3; i++)
    {
        free(arr[i]);
    }
    return 0;
}