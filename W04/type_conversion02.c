#include <stdio.h>

int main()
{
    // float abc = 1. / 0.f;
    // printf("abc : %f \n", abc); // abc : inf

    int a, b;
    float c, d;

    printf("숫자 입력 ; ");
    scanf("%d %d", &a, &b);

    c = a / b;
    d = (float)a / b;

    printf("두 수 비율 ; %f %f\n", c, d);
}