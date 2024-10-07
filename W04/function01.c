// https://modoocode.com/26
// 문제 1
// 이 강좌 최상단에서 이야기 했던 마술 상자를 함수로 제작해보세요
// (난이도 : 못한다면 강좌를 다시 읽어보아야 할 것입니다)
#include <stdio.h>

int add_4(int a)
{
    a += 4;
    return a;
}

int main()
{
    int a, b;
    scanf("%d", &a);

    b = add_4(a);
    printf("%d + 4 = %d\n", a, b);
}