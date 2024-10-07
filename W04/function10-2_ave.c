// https://modoocode.com/28
// 문제 1
// 사용자로 부터 5 명의 학생의 수학, 국어, 영어 점수를 입력 받아서
// 평균이 가장 높은 사람 부터 평균이 가장 낮은 사람까지 정렬되어 출력하도록 하세요.
// 특히, 평균을 기준으로 평균 이상인 사람 옆에는 '합격',
// 아닌 사람은 '불합격' 을 출력하게 해보세요 (난이도 : 中上).

// 구조체를 이용한 방법으로 풀기
// 나중에 다시 봐야지

#include <stdio.h>

typedef struct
{
    int student_id;
    float average;
} Student;

void sorted(Student students[], int n);

int main()
{
    Student students[5];
    int grade[5][3]; // 각 학생의 점수를 저장할 배열
    int i, j, sum;

    // 학생 점수 입력 및 평균 계산
    for (i = 0; i < 5; i++)
    {
        sum = 0;
        printf("%d번 학생의 점수 (수학, 국어, 영어): ", i + 1);
        for (j = 0; j < 3; j++)
        {
            scanf("%d", &grade[i][j]); // 각 과목 점수 입력
            sum += grade[i][j];        // 점수 합계
        }
        students[i].student_id = i + 1;  // 학생 번호 저장
        students[i].average = sum / 3.0; // 평균 계산
    }

    sorted(students, 5); // 정렬 함수 호출

    return 0;
}

void sorted(Student students[], int n)
{
    int i, j;
    // 평균을 기준으로 내림차순 정렬
    for (i = 0; i < n - 1; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (students[i].average < students[j].average) // 평균이 큰 순서대로
            {
                Student temp = students[i];
                students[i] = students[j];
                students[j] = temp;
            }
        }
    }

    // 전체 평균 계산
    float totalSum = 0;
    for (i = 0; i < n; i++)
    {
        totalSum += students[i].average; // 학생들의 평균 점수를 더함
    }
    float totalAve = totalSum / n; // 전체 평균 계산

    // 결과 출력
    for (i = 0; i < n; i++)
    {
        printf("%d번 학생의 평균: %.2f ", students[i].student_id, students[i].average);
        if (students[i].average >= totalAve) // 평균 이상인지 확인
        {
            printf("합격\n");
        }
        else
        {
            printf("불합격\n");
        }
    }
}
