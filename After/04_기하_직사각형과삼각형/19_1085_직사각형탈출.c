// https://www.acmicpc.net/problem/1085

/* x, y 좌표에서 w, h 직사각형의 경계선까지 가는 거리의 최소값을 구하는 문제 */
/* 1 ≤ x ≤ w-1, 1 ≤ y ≤ h-1 */

#include <stdio.h>

/* 최소값을 구하는 함수 */
int min(int a, int b)
{
    return a < b ? a : b;
}

int main()
{
    int x, y, w, h;
    scanf("%d %d %d %d", &x, &y, &w, &h);

    // x 에서 0, 0 과 w, h 까지 길이 비교
    int min_x = min(x, w - x);
    int min_y = min(y, h - y);

    printf("%d\n", min(min_x, min_y));

    return 0;
}

/* 기존에 작성했던 코드
#include <stdio.h>

int main()
{
    int x, y, w, h;
    scanf("%d %d %d %d", &x, &y, &w, &h);

    // 가로 길이 비교
    int min_x = w - x;
    if (min_x > x)
        min_x = x;

    // 세로 길이 비교
    int min_y = h - y;
    if (min_y > y)
        min_y = y;

    if (min_x > min_y)
        printf("%d\n", min_y);
    else
        printf("%d\n", min_x);
}
*/