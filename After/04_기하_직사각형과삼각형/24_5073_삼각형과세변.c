// https://www.acmicpc.net/problem/5073

/* 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면
삼각형의 조건을 만족하지 못 한다 (Invalid 출력)
세 변의 길이가 주어질 때 결과를 출력하는 문제
Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우 */
// 0 0 0 입력할 때까지 계속 반복

#include <stdio.h>

void what_kind_of_triangle(int a, int b, int c)
{
    /* 제일 긴 변 찾기 */
    int max = a;
    if (b > max)
        max = b;
    if (c > max)
        max = c;

    /* Case 4 */
    if (max >= a + b + c - max)
        printf("Invalid\n");

    /* Case 1 */
    else if (a == b && b == c)
        printf("Equilateral\n");

    /* Case 2 */
    else if (a == b || b == c || a == c)
        printf("Isosceles\n");

    /* Case 3 */
    else if (a != b && b != c && a != c)
        printf("Scalene\n");
}

int main()
{
    int a, b, c;
    /* scanf 반환값 개수와, 모든 값이 0 인지 동시에 확인 */
    while (scanf("%d %d %d", &a, &b, &c) == 3 && (a || b || c))
    {
        what_kind_of_triangle(a, b, c);
    }
    return 0;
}