#include <stdio.h>

#define MAX 100

int main()
{
    int num_students;
    char names[MAX][20]; // 학생 이름 저장 (최대 20자)
    int scores[MAX];     // 학생 성적 저장
    int i, j;

    // 학생 수 입력
    printf("학생 수를 입력하세요: ");
    scanf("%d", &num_students);

    // 학생 이름과 성적 입력
    for (i = 0; i < num_students; i++)
    {
        printf("%d번째 학생의 이름을 입력하세요: ", i + 1);
        scanf("%s", names[i]);
        printf("%s의 성적을 입력하세요: ", names[i]);
        scanf("%d", &scores[i]);
    }

    // 성적 막대 그래프 출력
    printf("\n학생 성적 막대 그래프:\n");
    for (i = 0; i < num_students; i++)
    {
        printf("%s: ", names[i]);
        for (j = 0; j < scores[i]; j++)
        {
            printf("*");
        }
        printf(" (%d)\n", scores[i]);
    }

    return 0;
}
