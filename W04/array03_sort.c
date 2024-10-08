// https://modoocode.com/18
#include <stdio.h>

int main()
{
    int student[10]; // 성적 배열
    int i, j, temp;  // for 문과 임시 변수

    for (i = 0; i < 10; i++)
    {
        printf("%2d 성적 ; ", i + 1);
        scanf("%d", &student[i]);
    }

    for (i = 0; i < 10 - 1; i++)
    {
        for (j = 0; j < 10 - i - 1; j++)
        {
            if (student[j + 1] > student[j])
            {
                temp = student[j + 1];
                student[j + 1] = student[j];
                student[j] = temp;
            }
        }
    }

    printf(" 성적 순 정렬 \n");
    for (i = 0; i < 10; i++)
    {
        printf("%2d 성적 %d \n", i + 1, student[i]);
    }
}