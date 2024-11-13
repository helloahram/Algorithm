// https://modoocode.com/33
// 문제1. 길이가 최대 100 인 문자열을 하나 입력 받아서
// 문자열을 역순으로 출력하는 함수를 만들어보세요. (난이도 : 下)
// 예를 들어서 "abcde" 입력 --> "edcba" 출력

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *reverse_string(char *str)
{
    // 인자로 전달받은 문자열 길이 구하기
    int length_str = strlen(str);

    // return 해줄 문자열 포인터 선언 + 동적 메모리 할당
    char *reversed = (char *)malloc((length_str + 1) * sizeof(char));
    if (reversed == NULL) // 메모리 할당 오류
    {
        fprintf(stderr, "메모리 할당 실패\n");
        exit(1); // 프로그램 종료 (또는 다른 방식으로 처리 가능)
    }

    for (int i = 0; i < length_str; i++)
    { // 역순으로 저장
        reversed[i] = str[length_str - 1 - i];
    }

    reversed[length_str] = '\0';
    return reversed; // 변경한 문자열 주소 반환
}

int main()
{
    char str[10] = "abcd";
    // scanf("%s", str);

    printf("기존 문자열 - %s\n", str);

    // 포인터 변수 선언하고 함수 호출
    /* reverse_string 함수가 malloc 을 이용해서
    힙에 문자열을 저장하고 그 메모리 주소를 반환하기 때문에
    포인터 변수로 이 힙 메모리 주소를 받아 접근한다 */
    char *reversed = reverse_string(str);
    printf("변경 문자열 - %s\n", reversed);
    free(reversed);

    return 0;
}

// 처음에 void 함수로 선언하려고 했는데
// 불완전한 형식 void 를 허용되지 않는다고 해서
// char* 반환으로 변경했다
// void *reverse_string2(char *str)
// {
//     // 문자열의 길이를 구해서 문자열 끝부터 처음까지
//     // 한 글자씩 출력하기
//     int length_str = strlen(str);
//     for (int i = length_str - 1; i >= 0; i--)
//     {
//         putchar(str[i]);
//     }
//     putchar('\n'); // 문자열 끝나고 줄바꿈해주기
// }