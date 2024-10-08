#include <stdio.h>

int main()
{
    float f;
    int i;

    printf("실수 ; ");
    scanf("%f", &f);

    i = (int)(f * 100) % 100;

    printf("i = %d\n", i);
}