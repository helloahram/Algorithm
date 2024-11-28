// https://www.acmicpc.net/problem/10101

/* 삼각형의 세 각을 입력 받고, 삼각형의 종류를 출력하는 문제
세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error */

#include <stdio.h>

void triangle(int a, int b, int c)
{
    /* Case 4. 세 각의 합이 180 이 아닌 경우 */
    if (a + b + c != 180)
        printf("Error\n");

    /* Case 1. 세 각의 크기가 모두 60 인 경우 */
    else if (a == 60 && b == 60 && c == 60)
        printf("Equilateral\n");

    /* Case 2. 두 각이 같은 경우 */
    else if (a == b || b == c || a == c)
        printf("Isosceles\n");

    /* Case 3. 같은 각이 없는 경우*/
    else if (a != b && b != c && a != c)
        printf("Scalene\n");
}

int main()
{
    int a, b, c;
    // scanf("%d %d %d", &a, &b, &c);
    // scanf 입력 오류 처리 추가
    if (scanf("%d %d %d", &a, &b, &c) != 3)
    {
        printf("Invalid Input\n");
        return 1;
    }

    triangle(a, b, c);
    return 0;
}