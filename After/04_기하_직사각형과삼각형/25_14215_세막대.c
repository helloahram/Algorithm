// https://www.acmicpc.net/problem/14215

/* 막대의 길이를 마음대로 줄일 수 있는 a, b, c 세 막대를 이용해서
아래 조건을 만족하는 삼각형을 만드는 문제
각 막대의 길이는 양의 정수이다
세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다
삼각형의 둘레를 최대로 해야 한다 */

/* 제일 긴 변이 다른 변의 합보다 같거나 크면 삼각형이 될 수 없다
적어도 두 변의 합보다 1 작아야 한다 */

#include <stdio.h>

int max_compass(int a, int b, int c) {
    /* a 가 제일 길다고 가정 */
    int max = a;
    int second = b, third = c;
    if (b > max) { /* b 가 제일 길다고 가정 */
        max = b;
        second = a, third = c;
    }
    if (c > max) { /* c 가 제일 길다고 가정 */
        max = c;
        second = a, third = b;
    }

    /* 제일 긴 변이 다른 두 변의 합보다 같거나 큰 경우 */
    if (max >= second + third) {
        max = second + third - 1;
        return max + second + third;
    } else /* 아니면 그냥 합쳐준다 */
    {
        return max + second + third;
    }
}

int main() {
    int a, b, c;
    // scanf("%d %d %d", &a, &b, &c);
    if (scanf("%d %d %d", &a, &b, &c) != 3 || a <= 0 || b <= 0 ||
        c <= 0) { /* 입력 유효성 검사 */
        printf("Invalid Input\n");
        return 1;
    }

    printf("%d\n", max_compass(a, b, c));
}