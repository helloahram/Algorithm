// https://www.acmicpc.net/problem/2745
// 24.11.02 SAT
// B진법 수 N이 주어졌을 때 이 수를 10진법으로 출력하는 프로그램을 작성하시오

// n을 문자열로 받고, 글자의 아스키코드를 계산하고 취합한다
// 0 - 9 는 아스키코드 48 - 57 이니 숫자는 그대로 '0' 을 빼서 계산
// A - z 는 아스키코드 65 - 90 이니 'A' 를 빼고 10 을 더해서 계산

#include <stdio.h>
#include <string.h>
#include <math.h>

// 문자를 해당하는 숫자 값으로 변환
int char_to_value(char c)
{
    if ('0' <= c && c <= '9')
        return c - '0';
    else if ('A' <= c && c <= 'Z')
        return c - 'A' + 10;
    return -1; // 잘못된 입력이 들어온 경우 return -1
}

int main()
{
    int b, decimal = 0; // 10진법 결과를 담을 변수
    char n[31];         // B진법 수를 담은 N

    scanf("%s %d", n, &b);

    // n 의 길이만큼 for 문 돌기
    int len = strlen(n);
    for (int i = 0; i < len; i++)
    {
        // 호너의 방법을 사용한 진법 변환
        decimal = decimal * b + char_to_value(n[i]);
    }

    printf("%d\n", decimal);
}