// 24.10.30 WED
// 수평으로 일렬로 만들어진 5줄의 단어를 세로로 출력하기

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, j; // 반복문 변수

    char **word = (char **)malloc(sizeof(char *) * 5);
    for (i = 0; i < 5; i++)
    { // 15글자 + NULL == 16
        word[i] = (char *)malloc(sizeof(char) * 16);
    }

    // 글자 입력 받기
    for (i = 0; i < 5; i++)
    { // 문자열로 입력 받는 이유는 %s 형식을 사용하면
      // 입력된 문자열은 자동으로 NULL 문자 \0 로 종료되기 때문에
      // 배열의 크기를 넘지 않는 범위 내에서 쉽게 문자열을 다룰 수 있어서
        scanf("%s", word[i]);
    }

    // 글자 세로로 출력하기
    for (j = 0; j < 15; j++)
    {
        for (i = 0; i < 5; i++)
        {
            // NULL 종료 문자 확인
            if (word[i][j] != '\0')
                printf("%c", word[i][j]);
            else // NULL 인 경우 넘어감
                printf("");
        }
    }
    printf("\n");

    // 메모리 할당 해제
    for (i = 0; i < 5; i++)
        free(word[i]);
    free(word);

    return 0;
}
