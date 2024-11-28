// https://www.acmicpc.net/problem/2903

// 중앙 이동 알고리즘에서 정사각형을 이루는 점 4개를 고르는 문제
// 중복되는 점은 한 번만 저장한다

// 한참 고민하다가 보니 점의 개수는 (2^n+1)^2 이라고 한다
// n승은 pow(base, exponent) - math.h

#include <stdio.h>
#include <math.h>

int carculate_dot(int stage)
{
    // 점의 개수 계산 (2^n+1)^2 후 return
    int dot = pow(2, stage) + 1;
    return dot * dot;
}

int main()
{
    int stage; // 과정 선언 및 입력 받기
    while (1)
    {
        scanf("%d", &stage);

        // 제한 사항 1 <= stage <= 15
        if (stage >= 1 && stage <= 15)
        {
            break;
        }
        printf("1부터 15까지만 입력 가능\n");
    }

    // carculate_dot 바로 출력하기
    printf("%d\n", carculate_dot(stage));
    return 0;
}