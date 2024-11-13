// https://www.acmicpc.net/problem/11866
// N명의 사람이 앉아있고 순서대로 k번째 사람을 제거한다
// 한 사람이 제거되면 남은 사람들도 이루어진 원을 따라
// N명의 사람들이 모두 제거될 때까지 과정을 반복한다

// 배열을 선언해서 번호를 매기고 people[i] = i+1
// 현재 위치 index 에서 k-1 만큼 이동해서 그 사람 제거
// 현재 위치 이후의 사람들을 한 칸씩 앞으로 당기기

#include <stdio.h>
#include <stdlib.h>

int main()
{
    // n 사람 수, k 제거할 순서, i for문
    int n, k, i;

    scanf("%d %d", &n, &k);

    // 사람들을 저장할 배열
    int *people = (int *)malloc(sizeof(int) * n);
    for (i = 0; i < n; i++)
    { // 1번부터 번호 매기기
        people[i] = i + 1;
    }

    int index = 0;  // 현재 제거할 사람의 인덱스
    int remain = n; // 남은 사람 수 n명

    printf("<");

    while (remain > 0) // 사람들이 0이 될 때까지
    {                  // k번째 사람을 찾기 위해 현재 인덱스에서 k-1 만큼 이동
        index = (index + k - 1) % remain;
        printf("%d", people[index]);

        // 현재 위치 이후의 사람을 한 칸씩 당기고
        // 마지막에 중복된 사람 이전까지만 저장 (remain-1)
        for (i = index; i < remain - 1; i++)
        {

            people[i] = people[i + 1];
        }

        // 남은 사람이 1명 이상이면 , 출력
        if (remain > 1)
            printf(", ");

        remain--; // 남은 사람 수 감소
    }

    printf(">\n");

    free(people);
    return 0;
}