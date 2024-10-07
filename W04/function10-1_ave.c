// https://modoocode.com/28
// 문제 1
// 사용자로 부터 5 명의 학생의 수학, 국어, 영어 점수를 입력 받아서
// 평균이 가장 높은 사람 부터 평균이 가장 낮은 사람까지 정렬되어 출력하도록 하세요.
// 특히, 평균을 기준으로 평균 이상인 사람 옆에는 '합격',
// 아닌 사람은 '불합격' 을 출력하게 해보세요 (난이도 : 中上).

// 이 방법은 index 를 사용하여 좀 불편하긴 했음

#include <stdio.h>

void sorted(int (*pgrade)[3]);

int main()
{
    int grade[5][3];
    int i, j;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 3; j++)
        {
            scanf("%d", &grade[i][j]);
        }
    }
    sorted(grade);
}

void sorted(int (*pgrade)[3])
{
    int i, j, sum;
    int totalSum = 0;
    float ave[5];
    // 정렬 후 학생 인덱스를 저장할 배열
    int index[5] = {0, 1, 2, 3, 4};

    // 평균 구하기
    for (i = 0; i < 5; i++)
    {
        sum = 0; // 학생마다 sum 초기화
        for (j = 0; j < 3; j++)
        {
            sum += pgrade[i][j];
        }
        ave[i] = sum / 3.0;
        totalSum += ave[i];
    }
    int totalAve = totalSum / 5;

    // 평균을 기준으로 정렬하기
    for (i = 0; i < 5 - 1; i++)
    {
        for (j = i + 1; j < 5; j++)
        {
            if (ave[i] < ave[j])
            {
                // 평균 교환
                float tempAve = ave[i];
                ave[i] = ave[j];
                ave[j] = tempAve;

                // 인덱스 교환
                int tempIdx = index[i];
                index[i] = index[j];
                index[j] = tempIdx;
            }
        }
    }
    for (i = 0; i < 5; i++)
    {
        int idx = index[i];
        printf("%d 번 평균 %.2f ", idx + 1, ave[i]);
        if (ave[i] > totalAve)
        {
            printf("합격\n");
        }
        else
        {
            printf("불합격\n");
        }
    }
}