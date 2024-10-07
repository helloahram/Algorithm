#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int i, j;
    i = 3;
    j = 5;
    printf("i %d j %d\n", i, j);
    swap(&i, &j);

    printf("i %d j %d\n", i, j);
}