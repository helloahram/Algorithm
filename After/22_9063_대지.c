// https://www.acmicpc.net/problem/9063

/* 구슬 n 개가 주어질 때, 구슬이 있는 모든 지점을 포함하는
가장 작은 남북, 동서 방향으로 평행한 변을 갖는 직사각형의 넓이를 구하는 문제 */

/* 가장 큰 x 와 y 에서 가장 작은 x 와 y 를 빼고,
그 차이를 곱해서 넓이를 구하면 되겠다 */

#include <stdio.h>

#define MAX 10000
#define MIN -10000

/* 최소값을 구하는 함수 */
int min(int a, int b)
{
    return a < b ? a : b;
}

/* 최대값을 구하는 함수 */
int max(int a, int b)
{
    return a > b ? a : b;
}

int main()
{
    int n; // 구슬의 개수
    scanf("%d", &n);

    int min_x = MAX, min_y = MAX; // x, y 최소값
    int max_x = MIN, max_y = MIN; // x, y 최대값

    for (int i = 0; i < n; i++)
    {
        int x, y; // 입력 받을 x, y
        scanf("%d %d", &x, &y);

        min_x = min(x, min_x);
        min_y = min(y, min_y);
        max_x = max(x, max_x);
        max_y = max(y, max_y);
    }

    /* 점이 한 개면 0 */
    if (n == 1)
        printf("0\n");
    else
    {
        int area = (max_x - min_x) * (max_y - min_y);
        printf("%d\n", area);
    }
}

/* 이런 방법도 있다고 한다 싱기방기 */
/*
void update_min_max(int x, int y, int *min_x, int *min_y, int *max_x, int *max_y) {
    *min_x = min(x, *min_x);
    *min_y = min(y, *min_y);
    *max_x = max(x, *max_x);
    *max_y = max(y, *max_y);
}

// main 함수 내에서 사용
update_min_max(x, y, &min_x, &min_y, &max_x, &max_y);
*/