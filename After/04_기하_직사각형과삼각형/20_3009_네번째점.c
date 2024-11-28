// https://www.acmicpc.net/problem/3009

/* 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해
필요한 네 번째 점을 찾는 문제 */

// 좌표끼리 짝꿍을 만들어 주면 된다

#include <stdio.h>

int main()
{
    int x1, x2, x3, y1, y2, y3;
    int x, y; // 네 번째 점
    scanf("%d %d", &x1, &y1);
    scanf("%d %d", &x2, &y2);
    scanf("%d %d", &x3, &y3);

    /* XOR 연산을 이용하여 중복되는 좌표를 제거하고
    남은 좌표를 찾는 방법도 있다 */
    x = x1 ^ x2 ^ x3;
    y = y1 ^ y2 ^ y3;

    /* 원래 작성했던 코드
        if (x1 == x2)
            x = x3;
        else if (x1 == x3)
            x = x2;
        else if (x2 == x3)
            x = x1;

        if (y1 == y2)
            y = y3;
        else if (y1 == y3)
            y = y2;
        else if (y2 == y3)
            y = y1;
    */

    printf("%d %d\n", x, y);
}