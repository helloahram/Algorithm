#include <stdio.h>

int main(void)
{
    int a = 10;  // 일반 변수 a 선언
    int *p = &a; // 포인터 변수 p 선언 및 a 주소값 할당

    printf("a = %d\n", a);
    printf("*p = %d\n", *p);

    printf("p = %p\n", p);
    printf("&a = %p\n", &a);
}
