#include <stdio.h>

int sum(int a, int b); // 함수 정의

int main()
{
    printf("%d\n", sum(1, 2));
}

int sum(int a, int b) // 함수 선언
{
    int result;
    result = a + b;
    return result;
}