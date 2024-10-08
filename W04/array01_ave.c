#include <stdio.h>

int main()
{
    int student[10]; // 성적을 입력 받을 배열
    int i, sum = 0;  // 인덱스와 총 합계

    for (i = 0; i < 10; i++)
    { // 성적 입력 받기
        printf("%d 번째 학생의 성적 ; ", i + 1);
        scanf("%d", &student[i]);
        sum += student[i];
    }

    int ave = sum / 10; // 평균 구하고 출력하기
    printf("전체 학생의 평균은 ; %d ", ave);

    for (i = 0; i < 10; i++)
    { // 평균 기준으로 합불 여부 출력하기
        printf("학생 %d ; ", i + 1);
        if (student[i] > ave)
            printf("합격\n");
        else
            printf("불합격\n");
    }
}