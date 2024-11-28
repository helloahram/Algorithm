/* https://modoocode.com/33
문제 2 길이가 최대 100 인 문자열을 입력 받아서 소문자는 대문자로,
대문자는 소문자로 출력하는 함수를 만들어보세요. (난이도 : 下)
예를 들어서 "aBcDE" 입력 --> "AbCde" 출력 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *modified(char *ori_str)
{
    int length = strlen(ori_str);
    char *mod_str = (char *)malloc((length + 1) * (sizeof(char)));

    for (int i = 0; i < length; i++)
    {
        // 대문자 A - Z 아스키 코드는 65 - 90
        if (65 <= ori_str[i] && ori_str[i] <= 90)
            mod_str[i] = ori_str[i] + 32;
        // 소문자 a - z 아스키 코드는 97 - 122
        else if (97 <= ori_str[i] && ori_str[i] <= 122)
            mod_str[i] = ori_str[i] - 32;
        else
            mod_str[i] = ori_str[i]; // 영어 외에는 그대로 유지
    }
    mod_str[length] = '\0'; // NULL 문자 추가
    return mod_str;
}

int main()
{
    char ori_str[10];
    fgets(ori_str, sizeof(ori_str), stdin);
    ori_str[strcspn(ori_str, "\n")] = '\0'; // 개행 문자 제거.

    printf("기존 문자열 - %s\n", ori_str);

    // 문자열 포인터 선언 및 함수 호출
    char *mod_str = modified(ori_str);

    printf("변경 문자열 - %s\n", mod_str);
    free(mod_str); // 동적 메모리 할당 해제

    return 0;
}
