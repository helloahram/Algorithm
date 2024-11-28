// https://www.acmicpc.net/problem/2292

// 육각형으로 이루어진 벌집이 있을 때 중앙의 방 1부터 N번방까지 가는
// 경로에서 최소 개수의 방을 구하는 문제

// 첫번째 계층 1개 - 마지막 번호 1
// 두번째 계층 6개 - 마지막 번호 7
// 세번째 계층 12개 - 마지막 번호 19
// 네번째 계층 18개 - 마지막 번호 37
// n번째 계층 6n개 - 마지막 번호 1 + 6 * n * (n-1)
// 주어진 숫자에서 n을 구하면 최소 경로를 구할 수 있다

// n = 1 + 6 * num * (num-1) 근의 공식으로 풀려다가 잘 안 됨
// 그래서 두번째 방법은, 반복문으로 n 구하기

#include <stdio.h>
#include <math.h>

int min_path(int num)
{
    if (num == 1)
    { // 1번 방이면 최소 경로는 1
        return 1;
    }

    int n = 1;         // 현재 계층
    int last_room = 1; // 현재 계층의 마지막 방번호

    // 주어진 방 번호가 계층의 마지막 방 번호를 넘을 때까지 반복
    // 왜냐하면 last_room 이 num 이상이면 num 이 해당계층에 포함되는 거니까
    while (last_room < num)
    { // n번째 계층의 마지막 방 번호까지 증가
        last_room += 6 * n;
        n++;
    }
    return n; // 주어진 방 번호 반환
}

int main()
{
    int num; // 방 번호 변수
    scanf("%d", &num);

    printf("%d\n", min_path(num));
}