// https://www.acmicpc.net/problem/11005

// 10진법 수 N을 B진법으로 바꿔 출력하는 프로그램

#include <stdio.h>
#include <string.h>

void decimal_to_b(int n, int b)
{
    char result[36]; // 결과를 저장할 배열
    int index = 0;

    while (n > 0) // n 이 0 보다 작아지면 종료
    {
        int remainder = n % b; // 나머지 계산
        // 나머지가 10보다 작으면 숫자이므로 '0' 을 더해주고
        // 나머지가 10보다 크면 A 를 더하고 10 을 빼줘서 알파벳을 만든다
        // 그 값을 result 에 저장하고 index +1 로 while 문 돌기
        if (remainder < 10)
            result[index++] = '0' + remainder;
        else
            result[index++] = 'A' + (remainder - 10);
        n /= b; // n 을 b 로 나눠서 계산 계속 하기
    }

    // 역순으로 결과 출력하기
    for (int i = index - 1; i >= 0; i--)
    {
        putchar(result[i]);
    }
    putchar('\n');
}

int main()
{
    int n, b;
    scanf("%d %d", &n, &b);

    decimal_to_b(n, b);

    return 0;
}