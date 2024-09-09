#include <stdio.h>

int main()
{
    int num[9];
    int i, max, count = 0;

    for (i = 0; i < 9; i++)
    {
        scanf("%d", &num[i]);
    }

    max = num[0];

    for (i = 1; i < 9; i++)
    {
        if (max < num[i])
        {
            max = num[i];
            count = i;
        }
    }

    printf("%d\n", max);
    printf("%d\n", count + 1);
}