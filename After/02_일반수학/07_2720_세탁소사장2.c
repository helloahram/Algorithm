// https://www.acmicpc.net/problem/2720

// 거스름돈의 액수가 주어지면 쿼터, 다임, 니켈, 페니의 개수를 구하는 프로그램
// 쿼터 0.25, 다임 0.10, 니켈 0.05, 페니 0.01, 거스름돈 1 <= C <= 500
// T testcase 개수, 거스름돈 C

// 거스름돈을 큰 액수부터 나눠서 몫을 구하고 나머지는 다음 액수로 나누면 되지 않을까?
// 거스름돈을 액수로 나눠서 몫이 생기면 액수를 구하면서 차례차례ㅡ

#include <stdio.h>

// 거스름돈의 액수를 동전의 개수로 나눠서 출력하는 함수
void change_change(int change)
{
    // change *= 100; // 100을 곱해서 정수로 계산하기 < 할 필요 없었음

    int coin[4] = {0};   // 동전 개수를 저장할 배열
    int remain = change; // 남는 거스름돈에 받은 거스름돈 대입

    // Quaters
    coin[0] = remain / 25;
    remain %= 25;

    // Dimes
    coin[1] = remain / 10;
    remain %= 10;

    // Nickels
    coin[2] = remain / 5;
    remain %= 5;

    // Pennies
    coin[3] = remain / 1;

    // 각 동전의 개수들 출력
    printf("%d %d %d %d\n", coin[0], coin[1], coin[2], coin[3]);
}

int main()
{
    int t, c; // Test Case 개수와 Change 변수 선언
    scanf("%d", &t);

    for (int i = 0; i < t; i++)
    { // Test Case 개수만큼 거스름돈 동전 구하기
        scanf("%d", &c);
        change_change(c);
    }
}