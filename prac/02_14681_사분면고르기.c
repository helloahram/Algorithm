#include <stdio.h>

int main()
{
    int p1, p2;
    scanf("%d %d", &p1, &p2);

    if (p1 > 0 && p2 > 0)
        printf("1\n");
    else if (p1 > 0 && p2 < 0)
        printf("4\n");
    else if (p1 < 0 && p2 > 0)
        printf("2\n");
    else if (p1 < 0 && p2 < 0)
        printf("3\n");

    return 0;
}