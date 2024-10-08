#include <stdio.h>

int main()
{

    int const size = 5;
    int student[size]; // 성적 배열
    int i, j, max;     // for 문과 최대값 변수
    for (i = 0; i < size; i++)
    {
        printf("%2d 성적 ; ", i + 1);
        scanf("%d", &student[i]);
    }

    printf("-----성적------\n");
    for (i = 0; i < size; i++)
    {
        printf(" %d 성적 ; ", i + 1);
        for (j = 0; j < student[i]; j++)
        {
            printf("*");
        }
        printf("\n");
    }
}
