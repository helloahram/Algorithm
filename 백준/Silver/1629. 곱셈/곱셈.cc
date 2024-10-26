// https://www.acmicpc.net/problem/1629
// A 를 B 번 곱한 수를 C 로 나눈 나머지를 구하는 문제

long long power(long long a, long long b, long long c)
{
    if (b == 0) // 재귀 종료 조건
        return 1;

    // 거듭 제곱 분할 - 지수를 반으로 줄여서 계산
    // a^(b/2) 를 계산하고 half 에 저장
    long long half = power(a, b / 2, c);
    // half 제곱 후 c 로 나눈 나머지 구하기
    half = (half * half) % c;

    // 홀수인 경우 한 번 더 곱하기
    if (b % 2 != 0)
        half = (half * a) % c;
    return half;
}

#include <stdio.h>
int main()
{
    // 입력받은 범위가 클 수 있으므로 long long
    long long a, b, c;
    scanf("%lld %lld %lld", &a, &b, &c);

    printf("%lld\n", power(a, b, c));
}
