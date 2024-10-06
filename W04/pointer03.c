// https://modoocode.com/25
#include <stdio.h>

int main()
{
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    int *parr = arr;
    int sum = 0;

    while (parr - arr <= 9)
    {
        sum += *parr;
        parr++;
    }
    printf("%d\n", sum);
    return 0;
}